title: Struktur
desc: "Semoga bisa dimengerti. :D"


## Konfigurasi

1. Meta / Root
	- File: `configs/meta.yaml`
	- Berisi konfigurasi website dan daftar tutorial.
	- URL: `/`
2. Tutorial
  	- File:  `configs / <tutorial>.yaml`
  	- Berisi konfigurasi _per_ tutorial dan daftar __cabang__ tutorial.
 	- URL: `/ <tutorial> /`
 	Untuk menambahkan jenis tutorial baru, harap hubungi siapa?
3. Cabang Tutorial
 	- File: `configs / <tutorial> / <cabang>.yaml`
 	- Isi: konfigurasi _cabang tutorial_, daftar (berutut) _seksi_ menu.
 	- URL: `/ <tutorial> / <cabang> /`
 	- Contoh pada tutorial _"code"_, salah satu cabang tutorial ini adalah _"c"_. URL-nya: `/ code / c /`
4. Halaman 
	- File: Tercantum di awal file laman
	- Isi: Judul, judul di menu, dan `seksi`-nya.


## Konten

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
	- URL: `/ <tutorial> / <cabang> /`. Contoh: `/code/c/`
	- konten: `pages / <cabang>.md`
	- isi konten: `pages / <cabang> / <0x00 s/d 0xFF>.md`