title: Struktur
desc: "Semoga bisa dimengerti. :D"


## Konfigurasi

1. Meta / Root
	- File: `configs/meta.yaml`
	- Berisi konfigurasi website dan daftar tutorial.
	- URL: `/`
2. Tutorial
  	- File:  `configs / <tutorial>.yaml`
  	- Berisi konfigurasi tiap tutorial dan daftar __cabang__ tutorial.
 	- URL: `/ <tutorial> /`
 	- Contoh: `configs / code.yml`
3. Cabang Tutorial
 	- File: `configs / <tutorial> / <cabang>.yaml`
 	- Isi: konfigurasi _cabang tutorial_, daftar (berutut) _seksi_ menu.
 	- URL: `/ <tutorial> / <cabang> /`
 	- Contoh: `configs / code / c.yaml` . URL-nya: `/ code / c /`


## Konten

Konten di website ini adalah konten yang ditampilkan tiap lamannya.
Konten yang ditampilkan didapat dari file `markdown` kecuali untuk konten halaman beranda/_home_ dan daftar `tutorial`.

Konten dari tutorial dan cabangnya adalah file markdown di direktori `pages`.

1. Root
	- URL: `/`
	- laman: `-`
	- konten: `tentang`
2. Tutorial
	- URL: `/ <tutorial> /`
	- laman: `-`
	- konten: 
3. Cabang Tutorial
	- URL: `/ <tutorial> / <cabang> /`.
	- Laman: `/ pages / <tutorial> / <cabang>.md`
4. Halaman Tutorial
	- File: Tercantum di awal file laman
	- Isi: `title` (Judul), `menu_title` (judul di menu), dan `bab`-nya.
	- Konten: `pages / <cabang> / <0x00 s/d 0xFF>.md`