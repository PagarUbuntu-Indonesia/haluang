import os
import sys
import flask
import yaml
from glob import glob

from flask_flatpages import FlatPages
from bs4 import BeautifulSoup as Soup

import pytest
from app import (
	app,
	hexnumber, 
	get_config,
)


def config_file(*args):
	"""
	path ke konfigurasi file
	"""
	page_path = path_properti()['config']
	c_path = "/".join([c for c in args if c is not None])
	c_path = os.path.normpath(c_path)
	return os.path.join(page_path, c_path)

def page_file(*args):
	"""
	path ke konten (markdown)
	"""
	page_path = path_properti()['page']
	a_path = "/".join([a for a in args if a is not None])
	a_path = os.path.normpath(a_path)
	return os.path.join(page_path, a_path)

def config_dari_konten(konten):
	config = {}
	fd = open(konten)
	for baris in fd.readlines():
		baris = baris.strip()
		# Sampai jumpa baris kosong
		if not baris:
			break
		config.update(yaml.load(baris))
	return config
	
def periksa_judul(req_data, konten):
	"""
	Periksa judul untuk konten yang pakai template `_base`
	"""
	soup = Soup(req_data, 'html.parser')
	judul = soup.find("div", attrs={'class': 'judul'})
	config_halaman = config_dari_konten(konten)
	return judul.text.strip() == str(config_halaman['title'])

def daftar_tutorial():
	site_config = get_config()
	for conf in site_config:
		if conf in ["title", "desc", "baseurl"]:
			continue
		else:
			yield conf

@pytest.fixture
def path_properti():
	"""
	Variabel direktori website
	"""
	import app
	return { 'config': getattr(app, 'CONFIG'),
		'page': getattr(app, 'PAGE'),
		'post': getattr(app, 'POST'),
		'template': getattr(app, 'TEMPLATE'),}

@pytest.fixture
def client():
	client = app.test_client()
	yield client

def test_hexnumber():
	"""
	Test generator angka hexa: 0x00 - 0xFF
	"""
	data = hexnumber()
	assert len(data) == len(range(0,256))
	for angka in data:
		assert int(angka, base=16) < 256 and int(angka, base=16) >= 0

def test_get_config():
	"""
	Tes konfigurasi dari
		meta > tutorial > cabang
	"""
	# file ga ada
	nodata = get_config("ga-ada.yaml")
	assert nodata == None

	data = get_config()
	assert data['title'] == "Haluang"
	assert data['desc']
	# ga usah pakai domain website, PENTING
	assert data['baseurl'] == "/"
	for tutor in data:
		if tutor in ["title", "desc", "baseurl"]:
			continue
		tutorial = data[tutor]
		assert tutorial['title'] # punya judul
		assert tutorial['desc'] # punya deskripsi
		assert tutorial['icon'] # punya ikon (dari font-awesome)
		if not tutorial['rilis']: # abaikan non rilis
			continue
		subdata = get_config("{}.yaml".format(tutor))
		for cabang in subdata:
			assert cabang['title']
			assert cabang['desc']
			if not cabang['rilis']:
				continue
			assert tutor in cabang['url']
			assert cabang['url'] != "#"
				

def test_tentang(client, path_properti):
	"""
	Tes toute "/tentang/"
	Kontennya pages/tentang.md
	"""
	konten = page_file("tentang.md")
	# ada file
	assert os.path.exists(konten)
	req = client.get('/tentang/')
	assert periksa_judul(req.data, konten)	

def test_404(client, path_properti):
	"""
	Tes toute "/404.html"
	Kontennya pages/404.md
	"""
	konten = page_file("404.md")
	# ada konten/file
	assert os.path.exists(konten)
	req = client.get('/404.html')

def test_index(client):
	"""
	Tes route "/"
	Hanya tutorial yang rilis ditampilkan
	"""
	req = client.get('/')
	req_data = str(req.data)
	site_config = get_config()
	soup = Soup(req.data, 'html.parser')
	for conf in daftar_tutorial():
		if not site_config[conf]['rilis']:
			judul = soup.find("div", attrs={"id":"tutorial-{}".format(conf)})
			assert judul == None
			continue

		# Data-data yang harus ada
		## Judul tutorial
		judul = soup.find("div", attrs={"id":"tutorial-{}".format(conf)})
		assert site_config[conf]['title'] in judul.text.strip()
		## Ikon
		ikon = judul.find("i")
		assert site_config[conf]['icon'] in ikon['class']

		# Data cabang-cabang tutorial
		tutorial_config = get_config("{}.yaml".format(conf))
		for item in tutorial_config[:3]:
			nama_class = "cabang-tutorial-{}".format(item['title'])
			cabang = soup.find('div',attrs={'id': nama_class})
			if item['rilis']:
				btn = cabang.find("a", attrs={'class': 'button'})
				# button class bukan `border--muted`
				assert "border--muted" not in btn['class']
				# teks button: "Buka"
				assert "Buka" in btn.text
				# url: / tutorial / cabang /
				assert item['url'] == btn['href'].strip()
			else:
				btn = cabang.find("a", attrs={'class': 'button'})
				# button class `border--muted`
				assert "border--muted" in btn['class']
				# teks button: "Segera"
				assert "Segera" in btn.text
				# url: #
				assert btn['href'].strip() == "#"
		
		# Selengkapnya
		nama_id = 'daftar-tutorial-' + conf
		print(nama_id)
		div = soup.find("div", attrs={'id': nama_id})
		tutorial_link = div.find("a")
		assert tutorial_link['href'].strip() == "/{}/".format(conf)

def test_tutorial(client, path_properti):
	"""
	Test rilis tutorial
	- menjarah dengan konfigurasi
	- menjarah dengan konten markdown
	url: `/ <tutorial> /`
	"""
	assert os.path.exists("{}/{}.html".format(
		path_properti['template'], 'tutorial'))
	site_config = get_config()
	for daftar in daftar_tutorial():
		t_config = get_config("{}.yaml".format(daftar))
		req = client.get("/{}/".format(daftar))
		soup = Soup(req.data, 'html.parser')

		if not site_config[daftar]['rilis']:
			continue
		# konfigurasi harus ada
		assert t_config != None

		# Data-data yang harus ada
		## Judul tutorial
		judul = soup.find("div", attrs={
			"class":"judul".format(daftar)})
		assert site_config[daftar]['title'] in judul.text.strip()
		## Ikon
		ikon = judul.find("i")
		assert site_config[daftar]['icon'] in ikon['class']

		jlh_cabang = len([x for x in t_config if x['rilis']])
		#jlh_baris
		baris = soup.find_all("div", attrs={'class':'contentMe'})
		if (jlh_cabang % 4 != 0) or (jlh_cabang < 4):
			jlh_baris = int(jlh_cabang / 4) + 1
			assert len(baris) == jlh_baris
		else:
			assert len(baris) == (jlh_cabang / 4)

		for cabang in t_config:
			nama_class = "cabang-tutorial-{}".format(cabang['title'])
			konten = soup.find('div',attrs={'id': nama_class})

			# deskripsi: mungkin berisi tag html
			if not cabang['rilis']:
				assert konten == None
			else:
				P = konten.find('p')
				assert Soup(cabang['desc'], 'html.parser').text\
					in P.text
		# Akhir for cabang
	# Akhir for daftar

def test_cabang_dan_itemnya(client, path_properti):
	"""
	Test cabang tutorial
	Tes tidak dijalankan di semua konten cabang
	URL: / <tutorial> / <cabang> / 
	     / <tutorial> / <cabang> / <HEX>
	"""
	site_config = get_config()

	# tutorial
	konfigurasi_tutorial = {}
	for t in daftar_tutorial():
		t_config = get_config("{}.yaml".format(t))
		if site_config[t]['rilis']:
			konfigurasi_tutorial[t] = t_config

	for per_cabang in konfigurasi_tutorial:
		for conf in konfigurasi_tutorial[per_cabang]:
			#print(conf)
			#print()
			if not conf['rilis']: 
				continue
			c_config = get_config("{}/{}.yaml".format(
				per_cabang, conf['nama']))
			assert c_config != None

			# Isi cabang 0x00 - 0xFF
			for h in hexnumber():
				md = page_file("pages", 
					per_cabang, conf['nama'], "{}.md".format(h))
				path = md.replace("pages/", "")
				req = client.get(path.replace(".md", ""))
				if not os.path.exists(md):
					assert req.status_code != 200
					continue
				assert req.status_code == 200
				

def test_daftar_menu_cabang(path_properti):
	"""
	test untuk daftar menu cabang dari kode html cabang

	- bab harus berurut
	- url harus menuju ke laman yang ada
	"""
	return