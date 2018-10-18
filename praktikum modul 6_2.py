Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Kegiatan 3. Operator
>>> Nama = 'Arya Mukti Araafi Z P'
>>> NIM = 'L200180151'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Fungsi type yaitu untuk mengetahui sebuah value masuk kedalam tipe data apa. Perintah type(a) berarti value a masuk ke dalam tipe data integer karena memuat angka.
>>> type(b)
<class 'int'>
>>> # Perintah di atas berarti value b masuk kedalam tipe data integer karena memuat angka.
>>> a / b
54.80952380952381
>>> # Perintah di atas berarti "a" dibagi "b". value a yaitu 1 + NIM[7:] sama dengan 1151 dan value b dengan fungsi len yang berarti jumlah suku kata Nama yaitu 21 maka "1151 / 21 = 54.80952380952381".
>>> a // b
54
>>> # Perintah di atas sama seperti sebelumnya hanya saja hasilnya akan dibulatkan ke bawah, berarti "a // b = 1151 // 21 = 54".
>>> 10 * (a - 999)
1520
>>> # Perintah di atas berarti "10 x (1151 - 999) = 1520"
>>> b ** 2
441
>>> # Perintah di atas berarti b = 21 dengan simbol ** yaitu pangkat yang berarti 21 pangkat 2 yang hasilnya 441.
>>> a % b
17
>>> # Simbol % pada perintah di atas yang berarti sisa hasil bagi. Jadi pada perintah a % b sama dengan pembagian 1151 dengan 21 sisa hasil baginya adalah 17.
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Perintah di atas menunjukan bahwa value c masuk kedalam tipe float karena memuat bilangan desimal(12.5)
>>> a / c
92.08
>>> # Perintah di atas berarti "a dibagi c = 1151 dibagi 12.5 = 92.08"
>>> a // c
92.0
>>> # Perintah di atas berarti "a dibagi c = 1151 dibagi 12.5 = hasilnya dibulatkan kebawah menjadi 92.0".
>>> a % c
1.0
>>> # Perintah di atas berarti "pembagian 1151 dengan 12.5 sisa hasil baginya adalah 1.0".
>>> c > b
False
>>> # Perintah di atas berarti c lebih besar dari b. Python merespon dengan kalimat "False" karena c(12.05) tidak lebih besar dari b(21).
>>> type(c > b)
<class 'bool'>
>>> # Perintah di atas menunjukan bahwa c > b merupakan tipe data bool karena memuat nilai True atau False.
>>> a > b and b > c
True
>>> # Python merespon dengan kalimat "True" karena a(1151) lebih besar dari b(21) dan b (21) lebih besar dari c(12.5).
>>> a > 1100 or b < 10
True
>>> # Python merespon dengan kalimat "True" karena a(1151) lebih besar dari 1100 walaupun b(21) lebih kecil dari 10 yang seharusnya false. Hal ini disebabkan oleh fungsi "or" yang beroperasi apabila antara "a" dan "b" sama dengan true maka python akan merespon dengan "True".
