title: SQLite
desc: "Ulasan Singkat SQLite"


## Tentang

> Singkatnya dari [Wikipedia](https://id.wikipedia.org/wiki/SQLite), __SQLite__ adalah sistem manajemen database tertanam (_embedded_), sangat ringan, tidak terlalu banyak installasi aplikasi, tidak perlu konfigurasi dan tidak membutuhkan server.

[Website SQLite](https://sqlite.org/)

Sqlite adalah sistem manajemen basis data relational yang bersifat opensource.
Sqlite, dengan kesederhanaannya, juga sarat fitur seperti sistem manajemen database yang lain:

- Ukuran paket Sqlite sangat kecil yang ukurannya kurang dari 500kb tidak seperti database lain.
- Sqlite bukan bertipe __client - server__, dia berupa pustaka memory yang bisa kita panggil langsung untuk menggunakannya
- Umumnya database sqlite disimpan pada file tunggal didalam harddrive komputer. semua obyek (table, view, triger, dll) sudah termasuk kedalam file tersebut.

## Penggunaan

- Database ringan seperti untuk embedded system, misalnya tv, smartphone, camera, home electronic
- Penyimpanan data temporary pada aplikasi

## Keuntungan

- _Free_ dan _opensource_
- _cross platform_
- Dukungan API yang luas untuk bahasa pemrograman lain, misalnya VB, C#, java, python, php, c++, dll
- Fleksibel

## Kekurangan

- Tidak mendukung _right outer join_ dan _full outer join_, hanya dukung _left outer join_
- Mode _view_ hanya untuk membaca
- Perintah _grant_ dan _revoke_ tidak diimplementasikan
- _Trigger_ hanya mendukung setiap baris, tidak di setiap pernyataan/_statement_

## Tanya Jawab

- Tanya: Apa ? <br/>
  Jawab: Gapapa

- Tanya: <br/>
  Jawab: 