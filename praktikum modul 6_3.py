Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Kegiatan 4. Tipe Data
>>> Nama = 'Arya Mukti Araafi Z P'
>>> NIM = 151
>>> Tinggi = 1.65
>>> Berat = 45
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Perintah di atas menunjukan bahwa a adalah tipe data tuple karena memuat deretan objek yang ditulis dalam tanda kurung.
>>> Aku[0]
2000
>>> # Perintah di atas menunukan indeks ke 0 pada baris "Aku" yaitu "TahunLahir(2000)"
>>> a = NIM % 4; Aku[a]
151
>>> # Perintah di atas berarti a = NIM % 4 ( sisa bagi 151 / 4 yaitu 3) Lalu dilanjutkan dengan perintah Aku[a] (Aku[3]) sama dengan tupple a indeks ke 3 yaitu "NIM = 151".
>>> type(Aku[a])
<class 'int'>
>>> # Perintah di atas menunjukan bahwa tupple A indeks a/3 masuk kedalam tipe data integer karena memuat angka.
>>> Aku[a:4]
(151,)
>>> # Perintah di atas merupakan slicing tupple Aku indeks a yaitu 151 dan indeks 3 yaitu simbol koma (,).
>>> type(Aku[4])
<class 'str'>
>>> # Perintah di atas menunjukan bahwa tupple Aku indeks 4 masuk kedalam tipe data string karena memuat simbol koma (,).
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Perintah di atas apabila dijalankan akan error karena elemen dalam tupple tidak bisa diganti.
>>> type(Data)
<class 'list'>
>>> # Perintah di atas menunjukan bahwa Data merupakan tipe data list karena memuat deretan objek yang ditulis dalam tanda kurung siku.
>>> type(Data[4])
<class 'str'>
>>> # Perintah di atas menunjukan bahwa list Data indeks 4 masuk kedalam tipe data string karena memuat huruf.
>>> Data[4][5]
'M'
>>> # Perintah di atas menunjukan bahwa list Data indeks 4 yaitu Nama lalu baris Nama indeks ke 5 yaitu "M".
>>> Data[4][a:6]
'a M'
>>> # Perintah di atas menunjukan bahwa list Data indeks 4 yaitu Nama lalu baris Nama slicing a sampai 6 yaitu "a M"
>>> Data[0] = 'ok'; Data
['ok', 45, 1.65, 151, 'Arya Mukti Araafi Z P']
>>> # Perintah di atas mengganti list Data indeks 0 yaitu TahunLahir diganti dengan kalimat 'ok' lalu dengan memanggil Data maka python merespon dengan menampilkan list Data yang sudah diganti menjadi ['ok', 45, 1.65, 151, 'Arya Mukti Araafi Z P'].
>>> Data[-a]
1.65
>>> # Perintah di atas menunjukan indeks yang diawali dengan tanda minus(-), maka indeks akan dibaca dari belakang mulai -1, -2, dst. Dengan memanggil list Data indeks -a makan akan menunjukan indeks -3 yaitu Tinggi(1.65)
>>> range(a)
range(0, 3)
>>> # Perintah di atas menunjukan fungsi range yaitu perulangan angka dimulai dari 0 sampai 3.
