#!/usr/bin/python
import os, sys
from flask import ( 
	abort, 
	Flask, 
	render_template, 
	url_for, 
	render_template_string
)
from flask_flatpages import (
	FlatPages, 
	pygmented_markdown, 
	pygments_style_defs
)
from flask_frozen import Freezer
import yaml
from markdown import markdown

CONFIG = 'configs'
PAGE = 'pages'
POST = 'posts'
STATIC = 'static'
TEMPLATE = 'templates'

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = '.'
FLATPAGES_MARKDOWN_EXTENSIONS = [
	'attr_list',	# {: #someid .someclass somekey='some value' }
	'def_list',		# Apple
					# :   Pomaceous fruit of plants of the genus 
					#     Malus in the family Rosaceae.
	'codehilite', 	# syntax highlight 
	'fenced_code', 	# github style syntax highlighting
	'smarty',		
	'smart_strong', # __strong__
	'tables',		# Table
]

app = Flask(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

def hexnumber():
	"""
	hasilkan angka hexadesimal 0 - 255
	dengan format: 0x00 s/d 0xFF
	"""
	st = ''
	res = []
	for x in range(256):
		if x < 0x10:
			st = '0{}'.format(str(hex(x))[-1])
		else:
			st = '{}'.format(hex(x))[2:]
		res.append('{}{}'.format('0x', st.upper()))
	return res

def get_config(filename = 'meta.yaml'):
	filename = os.path.join(CONFIG, filename)
	if not os.path.exists(filename):
		return
	with open(filename) as fd:
		return yaml.load(fd.read())

# override @app.route("/<tut>/<cab>/<item>")
@app.route('/static/<path:dirname>/<path:filename>')
def statis(dirname, filename):
	statik_file = '{}/{}'.format(dirname, filename)
	return app.send_static_file(statik_file)

@app.route('/')
def home():
	"""
	Tampilkan daftar tutorial
	dengan maksimal 3 cabangnya
	"""
	template = 'index.html'
	site_config = get_config()

	tutorial = {}
	for conf in site_config:
		if conf in ["title", "desc", "baseurl"]:
			continue
		# konfigurasi cabang
		tut_list = site_config[conf]
		if not tut_list['rilis']:
			continue
		tutorial[conf] = tut_list
		tutorial[conf]['konten'] = get_config("{}.yaml".format(conf))
	
	return render_template(template, 
		site=site_config, 
		tutorial=tutorial)

@app.route('/tentang/')
def tentang():
	template = "_base.html"
	path = '{}/{}'.format(PAGE, "tentang")
	page = pages.get_or_404(path)
	return render_template(template, 
		site = get_config(), 
		page=page)

@app.route("/404.html")
def not_found():
	template = "_base.html"
	path = '{}/{}'.format(PAGE, "404")
	page = pages.get_or_404(path)
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = page)

@app.route("/<item>/")
def tutorial(item):
	template = "tutorial.html"
	site_config = get_config()
	konfigurasi_tutorial = get_config(
		filename="{}.yaml".format(item))
	if not konfigurasi_tutorial:
		abort(404)
	return render_template(template, 
		site = site_config, 
		konfigurasi_meta = site_config[item],
		nama_tutorial = item,
		konfigurasi_tutorial = konfigurasi_tutorial )

#@app.route("/<tut>/<item>")
@app.route("/<tut>/<item>/")
def cabang(tut, item):
	template = "cabang.html"
	site_config = get_config()
	konf_cabang = get_config(filename="{}/{}.yaml".format(tut, item))
	
	if not konf_cabang:
		abort(404)
	path = '{}/{}/{}'.format(PAGE, tut, item)
	page = pages.get_or_404(path)
	daftar_bab, daftar_item = daftar_menu_cabang(
		site_config, konf_cabang, tut, item)
	return render_template(template,
		page = page,
		site = site_config, 
		konfigurasi_meta = site_config[tut],
		konfigurasi_tutorial = konf_cabang,
		daftar_bab = daftar_bab,
		daftar_item = daftar_item,
		nama_tutorial = tut,
		nama_cabang = item,
		nama_item = item,
		#url_item = url_for('item_cabang', tut=tut, cab=item, item=item)
	)

#@app.route("/<tut>/<cab>/<item>")
@app.route("/<tut>/<cab>/<item>/")
def item_cabang(tut, cab, item):
	template = "cabang.html"
	site_config = get_config()
	konf_cabang = get_config(filename="{}/{}.yaml".format(tut, cab))
	
	if not konf_cabang:
		abort(404)
	path = '{}/{}/{}/{}'.format(PAGE, tut, cab, item)
	page = pages.get_or_404(path)
	daftar_bab, daftar_item = daftar_menu_cabang(
		site_config, konf_cabang, tut, cab)
	return render_template(template, 
		page = page,
		site = site_config, 
		konfigurasi_meta = site_config[tut],
		konfigurasi_tutorial = konf_cabang,
		daftar_bab = daftar_bab,
		daftar_item = daftar_item,
		nama_tutorial = tut,
		nama_cabang = cab,
		nama_item = item,
		url_item = url_for('item_cabang', tut=tut, cab=cab, item=item)
	 )

def daftar_menu_cabang(konf_site, konf_cabang, tutorial, cabang):
	"""
	return (bab: [daftar item dari cabang]) # link ke hex
	"""
	konf_daftar_bab = konf_cabang['bab']
	
	daftar_bab = {}
	daftar_item = {}
	daftar_url = {}

	# Supaya gampang diurutkan di kode html
	for bab in konf_daftar_bab:
		daftar_bab[konf_daftar_bab[bab]['nomor']] = bab
		daftar_item[bab] = []

	for laman in pages:
		path = '{}/{}/{}'.format(PAGE, tutorial, cabang)
		if not laman.path.startswith(path) \
			or laman.path == path: # != <cabang>.md
			continue
		if 'bab' not in laman.meta:
			continue
		elif laman.meta['bab'] not in konf_daftar_bab:
			sys.stderr.write("[!] PERINGATAN: bab tidak terdaftar\n")
			sys.stderr.write("    bab : {}".format(laman.meta['bab']))
			sys.stderr.write("    file: {}".format(laman.path))
			continue

		daftar_item[laman.meta['bab']].append(laman)

	return daftar_bab, daftar_item

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		#app.run(host='0.0.0.0', debug=True)
		app.run(host='127.0.0.1', debug=True)
