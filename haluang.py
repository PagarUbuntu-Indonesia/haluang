#!/usr/bin/python3
import os
import sys
import glob
import yaml
import argparse
import app


DIR_KONF  = 'configs'
DIR_LAMAN = 'pages'
TEMPLATE  = "tutorial = 'code'\ncabang = 'golang'"

tut, cab = None, None

def init_cek():
	global tut, cab
	kurang = False
	try:
		import env
		tut, cab = env.tutorial, env.cabang
		log("tutorial: {}, cabang: {}".format(
			env.tutorial, env.cabang))
	except:
		error('perlu file: env.py', 'Format:', TEMPLATE)
		return False
	
	konfigurasi_error = "Nama file: {}"
	d, f = "", ""

	# Periksa konfigurasi meta/utama
	try:
		f = konfigurasi('meta')
		if not periksa(f):
			raise
	except: 
		error("Konfigurasi meta", 
			  konfigurasi_error.format(f))
		return False
	# Periksa konfigurasi tutorial
	try:
		f = konfigurasi(env.tutorial)
		if not periksa(f):
			raise
	except: 
		error("Konfigurasi tutorial",
			  konfigurasi_error.format(f))
		return False
	# Periksa konfigurasi cabang
	try:
		f = konfigurasi(env.tutorial, env.cabang)
		if not periksa(f):
			raise
	except: 
		error("Konfigurasi cabang",
			  konfigurasi_error.format(f))
		return False
	# Periksa laman <cabang>.md
	try:
		f = laman(env.tutorial, env.cabang)
		d = f.replace(".md", "")
		if not periksa(f) or not periksa(d):
			raise
	except: 
		error("Laman: {}".format(f),
			  "Directori: {}".format(d),
			  konfigurasi_error.format(f))
		return False

	return True

def periksa(konten):
	return os.path.exists(konten)

def konfigurasi(*args):
	p = DIR_KONF
	for arg in args:
		p = os.path.join(p, arg)
	p = "{}.yaml".format(p)
	return p

def get_konf_tutorial(tut):
	konf = {}
	data = app.get_config()
	for d in data:
		if d == tut:
			konf['meta'] = data[d]
			break
	data = app.get_config("{}.yaml".format(tut))
	konf['tutorial'] = data
	return konf

def get_konf_cabang(tut, cab):
	data = app.get_config("{}.yaml".format(tut))
	for d in data:
		if d['nama'] == cab:
			konf = d
			break
	return konf

def laman(*args):
	p = DIR_LAMAN
	for arg in args:
		p = os.path.join(p, arg)
	p = "{}.md".format(p)
	return p

def get_daftar_laman(tut, cab):
	dirname = "pages/{}/{}".format(tut, cab)
	hexn = app.hexnumber()
	daftar = []
	for h in hexn:
		fn = "{}/{}.md".format(dirname, h)
		if not periksa(fn):
			break
		daftar.append(h)
	return daftar

def error(*args):
	sys.stderr.write('[-] ERROR\n')
	for arg in args:
		sys.stderr.write(' '*4)
		sys.stderr.write(str(arg).replace("\n","\n    "))
		sys.stderr.write('\n')
	return -1

def log(*args):
	once = True
	sys.stderr.write('[+] ')
	for arg in args:
		if not once:
			sys.stderr.write(' '*4)
		once = False
		sys.stderr.write(str(arg).replace("\n","\n    "))
		sys.stderr.write('\n')

def peringatan(*args):
	sys.stderr.write('[!] PERINGATAN')
	for arg in args:
		sys.stderr.write(' '*4)
		sys.stderr.write(str(arg).replace("\n","\n    "))
		sys.stderr.write('\n')

def tambah(item):
	"""
	Menambahkan item dengan nama 
	setelah angka hexa terakhir
	"""
	item = laman(tut, cab, item)
	if item in get_daftar_laman(tut, cab) or periksa(item):
		error("Gagal menambahkan item. Item sudah ada",
			  "item: {}".format(item))
		return
	log("Menambahkan item: {}".format(item))
	
def selip():
	pass


if __name__ == '__main__':
	if not init_cek():
		sys.exit(1)
	parser = argparse.ArgumentParser(description="Manajemen Tutorial")
	parser.add_argument('item', type=str, help="item, 0x00 s/d 0xFF")
	parser.add_argument('aksi', choices=[
		'lihat',
		'tambah',
		'selip',
	])

	args = parser.parse_args()
