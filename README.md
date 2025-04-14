# Personal Portfolio

Website ini merupakan portfolio pribadi saya yang berisi tentang informasi diri saya.

## Ada apa saja isi dihalaman website saya?

1. Halaman home - Menampilkan ringkasan dari masing-masing halaman.
2. Halaman about - Menampilkan tulisan yang saya tulis.

## setelah itu saya menambahkan apps dan template pada project saya
1. apps yang pertama bernama berita 
2. dan yang kedua bernama peangguna
3. Menambahkan template dashboard
4. dan menambahkan template halaman

## Cara Menjalankan Project
1. buka cmd
2. lalu masuk kedalam folder website dan masuk ke direktorinya
3. setelah itu kita buat venv, saya memakai env. dengan mengetik 
```
py -m venv .venv
```
4. untuk mengaktifkannya, kita masuk ke folder env, masuk lagi ke folder Scripts, setelah itu kita ketik 
```
activate
```
5. kita sudah didalam lingkungkan virtual, setelah itu kita install django-nya dengan mengetik 
```
pip install django
```
6. dan kemudian kita membuat project baru django dengan mengetik  (saya menggunakan newwebsite)
```
django-admin startproject websiteku
```
7. setelah itu jika ingin membuat apps kita bisa mengetik
```
python manage.py startapp "kita dapat membuat sesuai keinginan kita"
```
8. serelah itu, untuk membuat migration kita dapat mengetikkan
```
python manage.py makemigrations "nama apps yang kita buat"
```
9. Setelah project dan apps telah dibuat dan untuk mengeceknya kita bisa mengetik 
```
py manage.py runserver
```