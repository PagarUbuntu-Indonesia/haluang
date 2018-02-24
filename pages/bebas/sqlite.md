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
- Penyimpanan data temporer aplikasi

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

- Tanya: Cocok buat DB besar? Kek AI ? <br/>
  Jawab: pertanyaan dia berat. Infonya ada [di sini](https://stackoverflow.com/questions/1033309/sqlite-for-large-data-sets). Untuk limitnya [di sini](https://www.sqlite.org/limits.html)

- Tanya: Kalo waktu load data nya bagaimana pak? misal 1 juta baris di file txt/csv, sama 1 juga baris di sqlite ? <br/>
  Jawab: Belum pernah coba, jadi belum bisa bandingin

- Tanya: kalo untuk json bagaimana, saya sih biasanya naro nya di file json, kalo dengan sqlite bagaimana, mana yang lebih efisien ? <br/>
  Jawab: Sepertinya, buat game bisa deh. Kemungkinan buat perangkat2 offline yang ga terkoneksi ke server. Ini [perbandingan kegunaan sqlite vs json](https://stackoverflow.com/questions/8652005/json-file-vs-sqlite-android) <br/>
  Ringkasan: Sqlite is mostly used when you want data to be saved and used in future. In your case data is changing every 5 minutes so its better to have JSON because every time to make the Database connection store and retrieve after 5 minutes will take some time.

## Info

- Lokasi: #ubuntu-indonesia @ freenode.net
- Silabus: [Silabus Belajar Bersama Sqlite Ubuntu indonesia](https://gist.github.com/taufiqur-rahman/f41af77c2cc81d226c158c800b7d221c)
- Brosur: [Brosur belajar bersama SQLite3 # ubuntu-indonesia](https://www.dropbox.com/s/dbh55fbdx91gs7y/browsur.png?dl=0)
- Pemateri: **Syandal_**

## Referensi

1. [sqlitetutorial.net](http://www.sqlitetutorial.net/)
2. [tutorialspoint.com/sqlite](https://www.tutorialspoint.com/sqlite/)
3. [guru99.com/sqlite-tutorial](http://www.guru99.com/sqlite-tutorial.html)