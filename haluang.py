#!/usr/bin/python3
import os
import sys
import glob
import yaml
import argparse
from app import get_config


DIR_KONF  = 'configs'
DIR_LAMAN = 'pages'
TEMPLATE  = "tutorial = 'code'\ncabang = 'golang'"

def tutorial_dikerjakan():
	kurang = False
	try:
		import env
		log("tutorial: {}, cabang: {}".format(
			env.tutorial, env.cabang))
	except:
		error('perlu file: env.py', 'Contoh:', TEMPLATE)
	
	konfigurasi_error = """file konfigurasi tidak ditemukan
	Nama file: {}"""
	f = ""
	try:
		f = konfigurasi('meta')
		if not periksa(f):
			raise
	except: 
		error(konfigurasi_error.format(f))
		return False

	try:
		f = konfigurasi(env.tutorial)
		if not periksa(f):
			raise
	except: 
		error(konfigurasi_error.format(f))
		return False
	try:
		f = konfigurasi(env.tutorial, env.cabang)
		if not periksa(f):
			raise
	except: 
		error(konfigurasi_error.format(f))
		return False

	return True
		
def path(*args):
	p = ""
	for arg in args:
		p = os.path.join(p, arg)
	return p

def periksa(konten):
	return os.path.exists(konten)

def konfigurasi(*args):
	p = path(DIR_KONF, *args)
	p = "{}.yaml".format(p)
	if not periksa(p):
		return ""
	return p

def laman(*args):
	p = path(DIR_LAMAN, *args)
	p = "{}.md".format(p)
	if not periksa(p):
		return ""
	return p

def error(*args):
	sys.stderr.write('[-] ERROR\n')
	for arg in args:
		sys.stderr.write(' '*4)
		sys.stderr.write(str(arg))
		sys.stderr.write('\n')
	return -1

def log(*args):
	once = True
	sys.stderr.write('[+] ')
	for arg in args:
		if not once:
			sys.stderr.write(' '*4)
		once = False
		sys.stderr.write(str(arg))
		sys.stderr.write('\n')

def peringatan(*args):	
	sys.stderr.write('[!] PERINGATAN')
	for arg in args:
		sys.stderr.write(' '*4)
		sys.stderr.write(str(arg))
		sys.stderr.write('\n')

def tambah():
	pass

def selip():
	pass


if __name__ == '__main__':
	if not tutorial_dikerjakan():
		sys.exit(1)
	parser = argparse.ArgumentParser(description="Manajemen Tutorial")
	parser.add_argument('aksi', choices=[
		'lihat',
		'tambah',
		'selip',
		'hapus',
	])

	args = parser.parse_args()