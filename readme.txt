# PYTHON GAME BY PULANGMEN

<img src="asset/preview/logo.png" width="100%">

## Deskripsi Game
Game “Koceng Loncat” adalah sebuah game sederhana yang menghadirkan pertualangan seru dari sudut pandang seekot kucing yang bisa melompat melewati rintangan. Game ini dikembangkan menggunakan library Pygame, yang merupakan library pemrograman dalam bahasa Python untuk membuat game 2D. Konsep permainan dari “Koceng Loncat” ialah pemain mengendalikan seekor kucing yang berlari secara otomatis di layar, dan tugas pemain adalah mengendalikan kucing tersebut untuk melompati rintangan dengan menggunakan tombol “space” yang muncul di jalannya. Pemain juga harus mendapatkan koin yang mencakupi untuk memainkan tema selanjutnya. 

## Dependensi atau Library
- pygame: Library utama untuk menjalankan game di python.
- random: Library untuk menghandle fungsi-fungsi yang bersifat random. 
- sys : Library untuk memberikan akses ke beberapa fitur sistem dan lingkungan pada Python.
- time: Library ini digunakan untuk menggenerate data waktu.
- json: Library ini digunakan unuk mengelola data dengen tipe data JSON.

## Menjalankan Game
Sebelum menjalankan game, pastikan semua paket atau library sudah terinstall:

```
# pip install pygame
# pip3 install pygame (alternative command)
```
Perintah untuk menjalankan game:
```
# python main.py
# python3 main.py (alternative command)
# py main.py (alternative command)
```

## Cara Bermain 

<img src="preview/home.png" width="100%">

Setelah game dijalankan, maka akan muncul tampilan menu utama seperti gambar di atas. Setelah itu, klik tombol untuk memulai permainan

<img src="preview/game-run.png" width="100%"> 

Setelah game dimulai player diharuskan menghindari rintangan yang ada dengan cara menekan tombol `space` unutk mendapatkan score sebanyak-banyaknya dan mengumpulkan koin sebanyak-banyaknya unutk membuka tema.

<img src="preview/game_over.png" width="100%"> 
Jika player mengenai rintangan maka game over dan data akan direcord dan player dapat memilih akan bermain lagi atau kembali ke home.

<img src="preview/menu_tema.png" width="100%"> 
<img src="preview/tema2_buy.png" width="100%"> 
<img src="preview/tema2.png" width="100%"> 
jika koin telah mencukupi player dapat membeli tema kedua dengan cara menekan tombol tema yang berada di pojok kanan atas pada menu home kemudian klik tombol buy dan tema kedua telah dibuka kemudian player dapat menggunakan kedua tema yang telah ada.


## Ketentuan Game
- Apabila player mengenai koin makan koin akan bertambah dan direcord setelah game over.
- Apabila game sedang berjalan dan player langsung pergi ke menu home maka data tidak akan direcord.
- Tujuan player mendapatkan skor dan koin sebanyak-banyaknya.
- Jika koin telah mencukupi player dapat membuka tema ke-2.
- Game Over: Terjadi apabila player mengenai rintangan yang ada.

## Kontrol Game
- `SPACE`: Digunakan untuk melompat menghindari rintangan dan mengumpulkan koin yang ada.
- `tombol setting`: Digunakan untuk menghentikan game sementara.


## Pengembang Game
 
| KELOMPOK : RB07 - KUCENG LONCAT |
| ---------------- |

| NIM  | Nama | Sebagai |
| ----- | --- | --- |
| 121140142  | FADHIL FIROOS  | Leader, Programmer, and Game Designer |
| 121140108  | Radot Yohanes Nababan  | Game Designer and Programmer |
| 121140071  | Maharani Triza Putri | Game Designer and Tester |
