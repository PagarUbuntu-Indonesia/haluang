title: Pengantar Pemograman Bahasa C

---


#### Alat dan Bahan <small>~ Pengguna GNU/Linux Debian dan Keluarga</small>
---

Alat yang diperlukan yaitu: _Compiler_, editor teks. Compiler yang kita gunakan yaitu **_GCC_**. Untuk teks editor, bisa kita gunakan teks editor yang telah tersedia seperti: **Vim, nano, Gedit, Kate, KWrite** atau lainnya.<br>
Pertama kita install GCC dan paket pendukungnya: `sudo apt-get install gcc`

> Untuk sistem operasi yang berbeda mohon menyesuaikan.
> Ada banyak tulisan untuk instalasi _compiler_ **_gcc_**.

#### Percobaan Membuat Program
---

Berikut kode untuk percobaan ini

```c
#include <stdio.h>

// Ini adalah sebaris komentar

/*
Ini beberapa baris komentar.
Komentar akan diabaikan oleh Compiler.
Komentar bisa kita gunakan sebagai catatan di dalam program kita.
*/

int main()
{
	printf("Program pertama saya\n");
	return 0;
}
```

#### Kompilasi
----

Syntax: `gcc <nama_file_kode_sumber> -o <hasil>`

```bash
$ gcc program.c -o program
```

#### Eksekusi Program
----

```bash
$ ./program
Program pertama saya
```
