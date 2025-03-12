# Personal Portfolio

Website ini merupakan portfolio pribadi saya yang berisi tentang informasi diri saya.

## Ada apa saja isi dihalaman website saya?

1. Halaman home - Menampilkan ringkasan dari masing-masing halaman.
2. Halaman about - Menampilkan tulisan yang saya tulis.

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
7. project telah dibuat dan untuk mengeceknya kita bisa mengetik 
```
py manage.py runserver
```