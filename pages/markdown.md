title: Penulisan Tutorial

---


> Tutorial penulisan tutorial ini masih _draft_

Ini adalah template yang biasa digunakan dalam penulisan tutorial. Ini adalah untuk mempermudah penulisan tutorial dengan sedikit tata cara yang disediakan di sini.

Selain mengunakan `concise.css versi 3` untuk memperindah tampilan, juga dibuat file `css` untuk website ini. Maka dengan keterbatasan pembuat website, maka digunakan tata cara ini untuk penyesuaian dengan `css` untuk website ini.


### Kepala / Sub-Judul {:.titleMe }

> Pastikan spasi seperti berikut: `###<SPASI>[FA-IKON]<SPASI>[JUDUL]<SPASI>{:.titleMe}`

#### _Default_
---

```markdown
### <i class="fa fa-info-circle"></i> Sub Judul {:.titleMe }

Isi subjudul. 
```
Ini adalah kepala _sub-judul_ dengan isi yang menjelaskan dalam bentuk tulisan bahasa pemograman yang digunakan.
Dalam satu judul/laman tutorial, biasa terdiri dari beberapa **_sub-judul_**.

#### Info
---

```markdown
### <i class="fa fa-info-circle"></i> Sub Judul {:.titleMe }
```

#### Kode
---

Isi **_sub-judul_** yang melampirkan kode, boleh gunakan **Kepala sub-judul_** ini.

```markdown
### <i class="fa fa-code"></i> Kode Program {:.titleMe }
```

#### Eksekusi Program
---

Isi **_sub-judul_** yang melampirkan kode, boleh gunakan **Kepala sub-judul_** ini.

```markdown
### <i class="fa fa-terminal"></i> Eksekusi Program {:.titleMe }
```

#### Daftar/_List_
---

```markdown
### <i class="fa fa-list"></i> Daftar {:.titleMe }
```


### <i class="fa fa-info-circle"></i> Sub Judul {:.titleMe }

Contoh kode **python**

``` python
from markdown.preprocessors import Preprocessor

class MyPreprocessor(Preprocessor):
	def run(self, lines):
		new_lines = []
		for line in lines:
			m = MYREGEX.match(line)
			if m:
				# do stuff
			else:
				new_lines.append(line)
		return new_lines
```

### <i class="fa fa-code"></i> Subjudul {:.titleMe }
---



### Test Section

---

 - ##### <i class="fa fa-file-code-o"></i> H5


## Header

#H1
## H2
### H3
#### H4
##### H5

Regular paragraf

__strong text__ and **another strong text**

_italic_ and *another italic text*

## List:

 1. satu
 2. dua

## Another List:

- satu
- dua

## Inline Code highlight

`code`
