#!/usr/bin/python
import os, sys
from glob import glob
from flask import (
	Flask, render_template, url_for, render_template_string)
from flask_flatpages import (
	FlatPages, pygmented_markdown, pygments_style_defs)
from flask_frozen import Freezer
import yaml
from markdown import markdown

TEMPLATE = 'templates'
PAGE 	= 'pages'
STATIC 	= 'static'
POST 	= 'posts'
CONFIG 	= 'configs'

def renderer(text, **kwargs):
	prerender = render_template(text, **kwargs)
	return pygmented_markdown(prerender)

def get_config(filename = 'meta.yaml'):
	filename = os.path.join(CONFIG, filename)
	return yaml.load(open(filename).read())

def hexnumber():
	st = ''
	res = []
	for x in range(256):
		if x < 0x10:
			st = '0{}'.format(str(hex(x))[-1])
		else:
			st = '{}'.format(hex(x))[2:]
		res.append('{}{}'.format('0x', st.upper()))
	return res
	

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
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
#FLATPAGES_HTML_RENDERER = renderer

app = Flask(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


def lang_menu(lang, konfigurasi):
	"""
	return: bab, <daftar laman per bab>
	
	id dipakai untuk pengurutan bab di menu
	dalam tiap bab, lampirkan <daftar laman per bab>
	"""
	bab = {}
	daftar_menu = {}
	konfigurasi = konfigurasi['seksi']
	for seksi in konfigurasi:
		bab [konfigurasi[seksi]['id']] = seksi
		daftar_menu[seksi] = []

	for p in pages:
		if p.path.startswith('pages/code/{}'.format(lang)) \
			and p.path != 'pages/code/{}'.format(lang):
			if p.meta['seksi'] not in konfigurasi:
				sys.stderr.write("[!] ERROR: seksi tidak ada di konfigurasi")
				sys.stderr.write("\n    seksi: {}".format(p.meta['seksi']))
				sys.stderr.write("\n    path : {}\n".format(p.path))
				continue

			daftar_menu[p.meta['seksi']].append(p)

	return bab, daftar_menu


@app.route('/')
def home():
	template = 'index.html'
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = None,
		codes = get_config(filename="code.yaml"))

# CODE
@app.route("/code/")
def code():
	template = "code.html"
	site_config = get_config()
	konten = get_config(filename="code.yaml")
	return render_template(template, 
		site 	= site_config, 
		page 	= site_config['code'],
		contents = konten )

@app.route("/code/<lang>")
@app.route("/code/<lang>/")
def code_lang(lang):
	"""
	url: BASEURL / code / lang
	cth: localhost:5000/code/c
	"""
	template = "prog_lang.html"
	path = '{}/{}/{}'.format(PAGE, "code", lang)
	site_config = get_config()
	lang_config = get_config('code/{}.yaml'.format(lang))
	page = pages.get_or_404(path)
	bab, daftar = lang_menu(lang, lang_config)
	return renderer(template, 
		site = site_config, 
		page = page,
		config = lang_config,
		bab = bab,
		daftar_menu = daftar)

@freezer.register_generator
def code_lang_urls():
	for lang in glob('pages/code/*.md'):
		lang = lang.replace('pages/code','')
		lang = lang.replace('.md',   '')
		if lang[0] == "/": lang = lang[1:]
		try:
			lang_config = get_config('code/{}.yaml'.format(lang))
			if not lang_config:
				raise Exception
		except:
			continue
		yield url_for('code_lang',lang=lang)

	hexa = hexnumber()
	for konten in glob('pages/code/*/*.md'):
		konten = konten.replace('pages/code','')
		konten = konten.replace('.md',   '')
		if konten[0] == "/": konten = konten[1:]
		lang, konten = konten.split("/")
		try:
			lang_config = get_config('code/{}.yaml'.format(lang))
			if not lang_config:
				raise Exception
			if konten not in hexa:
				raise Exception
		except:
			sys.stderr.write("[PERINGATAN]: {} tidak ditemukan".format(konten))
			continue
		yield url_for('code_lang_content',lang=lang, hexnum=konten)

@app.route("/code/<lang>/<hexnum>")
@app.route("/code/<lang>/<hexnum>/")
def code_lang_content(lang, hexnum):
	"""
	url: BASEURL / code / lang / hexnum 
	cth: localhost:5000/code/c/0x00
	"""
	template 	= "prog_lang.html"
	site_config = get_config()
	path = '{}/{}/{}/{}'.format(PAGE, "code", lang, hexnum)
	page = pages.get_or_404(path)
	lang_config = get_config('code/{}.yaml'.format(lang))
	current_lang_num = '/{}/{}/{}'.format("code", lang, hexnum)
	bab, daftar = lang_menu(lang, lang_config)
	return renderer(template, 
		site = site_config, 
		page = page,
		config = lang_config,
		bab = bab,
		daftar_menu = daftar, 
		laman_skrg = current_lang_num )


@app.route('/jinja/')
def jinja():
	template = '_jinja.html'
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = None)

@app.route("/markdown/")
def markdown():
	template = "_base.html"
	path = '{}/{}'.format(PAGE, "markdown")
	page = pages.get(path)
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = page)

@app.route("/tentang/")
def tentang():
	template = "_base.html"
	path = '{}/{}'.format(PAGE, "tentang")
	page = pages.get(path)
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = page)

@app.route("/404.html")
def not_found():
	template = "_base.html"
	path = '{}/{}'.format(PAGE, "404")
	page = pages.get(path)
	site_config = get_config()
	return render_template(template, 
		site = site_config, 
		page = page)

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
		#freezer.run(debug=True)
	else:
		app.run(host='0.0.0.0', debug=True)
