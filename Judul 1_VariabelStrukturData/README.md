# SISTEM PLAYLIST MUSIK
## DESKRIPSI SINGKAT
Program antrian playlist musik ini merupakan program sederhana berbasis Python yang menggunakan struktur data Singly Linked List untuk mengelola daftar lagu. Program menerapkan konsep Queue (FIFO / First In First Out), yaitu lagu yang pertama dimasukkan akan diputar pertama kali. Fitur utama program meliputi menambahkan lagu ke playlist, memutar lagu dari urutan terdepan, menampilkan seluruh daftar playlist, dan keluar dari program. Setiap lagu disimpan dalam bentuk node yang saling terhubung menggunakan pointer next, sehingga data dapat dikelola secara dinamis dan efisien.

## Source Code
<img width="379" height="78" alt="WhatsApp Image 2026-04-29 at 00 24 57" src="https://github.com/user-attachments/assets/d46ae1fd-fcd1-49b7-b732-9cc61481ab82" />
Paragraf kode ini digunakan untuk membuat class Node. Node merupakan elemen dasar dalam linked list yang digunakan untuk menyimpan data lagu dan alamat node berikutnya. Variabel self.lagu berfungsi menyimpan judul lagu, sedangkan self.next digunakan sebagai pointer yang menghubungkan node saat ini dengan node berikutnya. Nilai awal next adalah None karena node belum terhubung dengan node lain.
<img width="348" height="88" alt="WhatsApp Image 2026-04-29 at 00 26 45" src="https://github.com/user-attachments/assets/af6c63b2-2d0d-4f24-b4b4-bc3943622909" />
Paragraf ini digunakan untuk membuat class PlaylistQueue, yaitu class utama yang mengatur sistem antrian playlist musik. Variabel front digunakan untuk menunjuk node paling depan dalam queue, sedangkan rear digunakan untuk menunjuk node paling belakang. Pada awal program, kedua variabel bernilai None karena playlist masih kosong dan belum memiliki lagu.
<img width="445" height="62" alt="WhatsApp Image 2026-04-29 at 00 29 05" src="https://github.com/user-attachments/assets/5352e29e-e618-4ec9-9bd1-29b53fecb9cf" />
Paragraf ini merupakan fungsi untuk menambahkan lagu baru ke playlist. Program terlebih dahulu membuat objek node baru berdasarkan judul lagu yang dimasukkan pengguna. Node baru tersebut nantinya akan dimasukkan ke dalam antrian playlist.
<img width="579" height="68" alt="WhatsApp Image 2026-04-29 at 00 30 21" src="https://github.com/user-attachments/assets/178ee137-4e9c-4283-ac07-9c7a531f3c9e" />
Paragraf ini digunakan untuk mengecek apakah playlist masih kosong. Jika kosong, maka node baru akan menjadi node pertama dalam linked list. Oleh karena itu, pointer front dan rear sama-sama diarahkan ke node baru karena hanya ada satu lagu dalam playlist.
<img width="769" height="97" alt="WhatsApp Image 2026-04-29 at 00 31 59" src="https://github.com/user-attachments/assets/6b84a167-6c0c-4c51-bd09-7bcd9ee3ae58" />
Paragraf kode ini dijalankan ketika playlist sudah memiliki lagu. Program menghubungkan node terakhir (rear) ke node baru menggunakan pointer next. Setelah itu, pointer rear dipindahkan ke node baru agar rear tetap menunjuk node paling belakang dalam queue. Fungsi print ini digunakan untuk menampilkan pesan bahwa lagu berhasil dimasukkan ke dalam playlist. Pesan ini memberikan informasi kepada pengguna bahwa proses penambahan data berhasil dilakukan.
<img width="621" height="103" alt="WhatsApp Image 2026-04-29 at 00 34 57" src="https://github.com/user-attachments/assets/2a711488-23df-4011-8bb5-df5bce10716c" />
def putar_lagu(self): merupakan fungsi untuk memutar lagu paling depan dalam antrian. Fungsi ini menerapkan konsep dequeue pada queue, yaitu mengambil dan menghapus data dari bagian depan. Paragraf ini digunakan untuk memeriksa apakah playlist kosong sebelum lagu diputar. Jika queue kosong, program akan menampilkan pesan bahwa playlist kosong dan fungsi langsung dihentikan menggunakan return.
<img width="456" height="55" alt="WhatsApp Image 2026-04-29 at 00 37 25" src="https://github.com/user-attachments/assets/927053fa-5468-4a8c-b6f7-e8c61b092cbb" />
Paragraf kode ini digunakan untuk mengambil data lagu dari node paling depan. Lagu tersebut kemudian ditampilkan sebagai lagu yang sedang diputar.
<img width="537" height="37" alt="WhatsApp Image 2026-04-29 at 00 38 16" src="https://github.com/user-attachments/assets/d11e0506-fe96-4764-8d89-96fcb26ef50e" />
Paragraf ini digunakan untuk menghapus node paling depan dari queue. Caranya adalah dengan memindahkan pointer front ke node berikutnya. Dengan demikian, lagu yang sudah diputar otomatis keluar dari antrian.
<img width="390" height="53" alt="WhatsApp Image 2026-04-29 at 00 39 24" src="https://github.com/user-attachments/assets/cb92fadc-3e9d-44f0-b810-d76a34ceec8b" />
Paragraf ini digunakan untuk memeriksa apakah playlist menjadi kosong setelah lagu diputar. Jika semua lagu sudah habis, maka pointer rear juga diubah menjadi None agar queue kembali ke kondisi kosong.
<img width="545" height="116" alt="WhatsApp Image 2026-04-29 at 00 40 36" src="https://github.com/user-attachments/assets/459283dd-3bb9-43fb-a8bf-dc784a36b0c9" />
def tampilkan_playlist(self): Paragraf ini merupakan fungsi untuk menampilkan seluruh isi playlist musik yang tersimpan dalam linked list. Paragraf ini digunakan untuk mengecek apakah playlist kosong. Jika tidak ada lagu, program menampilkan pesan bahwa playlist masih kosong dan fungsi dihentikan.
<img width="529" height="68" alt="WhatsApp Image 2026-04-29 at 00 42 43" src="https://github.com/user-attachments/assets/9b91b1d0-fd20-4604-a1e8-0cb24f184273" />
Paragraf ini digunakan untuk proses traversal linked list. Variabel current berfungsi sebagai pointer sementara untuk menelusuri node dari depan, sedangkan variabel nomor digunakan untuk memberikan nomor urut pada daftar lagu.
<img width="639" height="89" alt="WhatsApp Image 2026-04-29 at 00 43 50" src="https://github.com/user-attachments/assets/4426105e-b375-4221-ba68-2429ba898506" />
Paragraf kode ini digunakan untuk menampilkan seluruh lagu dalam playlist. Program melakukan traversal dari node pertama hingga node terakhir. Pada setiap perulangan:
lagu ditampilkan, pointer current berpindah ke node berikutnya, nomor urut bertambah satu. Perulangan berhenti ketika current bernilai None.
<img width="479" height="66" alt="WhatsApp Image 2026-04-29 at 00 47 17" src="https://github.com/user-attachments/assets/d0976c0a-7819-4f85-91c2-716bdc9a2829" />
Paragraf ini digunakan untuk membuat objek queue bernama playlist. Objek ini digunakan untuk menjalankan seluruh fungsi dalam class PlaylistQueue.
<img width="413" height="30" alt="WhatsApp Image 2026-04-29 at 00 48 21" src="https://github.com/user-attachments/assets/8b6e88ae-84c5-4144-8add-81133fea8597" />
Paragraf ini merupakan perulangan utama program. Program akan terus berjalan dan menampilkan menu sampai pengguna memilih keluar.
<img width="727" height="109" alt="WhatsApp Image 2026-04-29 at 00 49 10" src="https://github.com/user-attachments/assets/1719ecd1-7053-42b3-9066-ca8d75ca9529" />
Paragraf ini digunakan untuk menampilkan pilihan menu kepada pengguna agar pengguna dapat memilih fitur yang ingin dijalankan.
<img width="515" height="37" alt="WhatsApp Image 2026-04-29 at 00 50 08" src="https://github.com/user-attachments/assets/fa9efc6d-b4f2-4055-ba9e-858b7a5636b5" />
Paragraf ini digunakan untuk menerima input pilihan menu dari pengguna.
<img width="563" height="339" alt="WhatsApp Image 2026-04-29 at 00 51 36" src="https://github.com/user-attachments/assets/1fef6c94-16b1-425b-9ec1-37fd5d6bf138" />
Ketika pengguna memilih menu 1. Program meminta input judul lagu lalu memanggil fungsi tambah_lagu() untuk memasukkan lagu ke playlist. Ketika pengguna memilih menu 2. Program memanggil fungsi putar_lagu() untuk memutar dan menghapus lagu paling depan. ketika pengguna memilih menu 3. Maka akan menampilkan seluruh isi playlist dengan memanggil fungsi tampilkan_playlist(). ketika pengguna memilih menu 4. Program menampilkan pesan selesai lalu menghentikan perulangan menggunakan break. Jika pengguna memasukkan angka selain 1–4, program akan menampilkan pesan bahwa pilihan tidak valid.

## Output Program
<img width="481" height="530" alt="WhatsApp Image 2026-04-29 at 01 02 27" src="https://github.com/user-attachments/assets/27c3d2d1-c449-49d9-a8ab-91c746d1a8fd" />
Pada tampilan awal, program menampilkan menu utama yang berisi beberapa pilihan, yaitu menambah lagu, memutar lagu, menampilkan playlist, dan keluar dari program. Pengguna kemudian memilih menu 1 untuk menambahkan lagu ke dalam playlist.
Saat pengguna memasukkan judul lagu seperti evaluasi, program berhasil menambahkan lagu tersebut ke dalam antrian playlist dan menampilkan pesan:
Lagu 'evaluasi' berhasil ditambahkan ke playlist.
Pesan tersebut menandakan bahwa node baru berhasil dibuat dan dimasukkan ke bagian belakang linked list. Setelah itu program kembali menampilkan menu utama karena program menggunakan perulangan while True, sehingga pengguna dapat terus melakukan operasi lainnya.
Pada proses berikutnya, pengguna kembali memilih menu 1 dan memasukkan lagu rayuan perempuan gila. Program kembali menambahkan lagu tersebut ke bagian belakang antrian playlist. Hal ini menunjukkan bahwa queue bekerja dengan konsep FIFO (First In First Out), yaitu lagu pertama yang masuk akan berada di bagian depan, sedangkan lagu baru selalu ditambahkan di belakang.
Kemudian pengguna kembali menambahkan lagu titik nadir.
Dari struktur tersebut menunjukakan bahwa front menunjuk lagu pertama yaitu evaluasi, dan rear menunjuk lagu terakhir yaitu titik nadir.
Artinya, jika menu putar lagu dijalankan, maka lagu evaluasi akan diputar terlebih dahulu karena berada di posisi paling depan dalam queue.
<img width="500" height="303" alt="WhatsApp Image 2026-04-29 at 01 03 48" src="https://github.com/user-attachments/assets/6699df6b-811d-4341-b40a-ff6976d55468" />
Output program di atas menunjukkan proses pemutaran lagu, penampilan playlist, dan penghentian program pada sistem antrian playlist musik menggunakan Singly Linked List dan konsep Queue (FIFO).
Pada bagian awal output, program menampilkan pesan: 
Sedang memutar: evaluasi
Pesan ini muncul karena pengguna memilih menu 2 yaitu Putar Lagu. Program kemudian mengambil lagu yang berada di posisi paling depan (front) pada queue, yaitu lagu evaluasi. Setelah lagu diputar, node tersebut dihapus dari linked list dengan cara memindahkan pointer front ke node berikutnya.
Selanjutnya program kembali menampilkan menu utama karena menggunakan perulangan while True. Pengguna kemudian memilih menu 3 untuk menampilkan playlist. Program menampilkan isi playlist yang tersisa:
1. rayuan perempuan gila
2. titik nadir
Output tersebut menunjukkan bahwa lagu evaluasi sudah berhasil dihapus dari queue setelah diputar, sehingga playlist sekarang hanya berisi dua lagu yang tersisa.
Pada bagian akhir, pengguna memilih menu 4 untuk keluar dari program. Program menampilkan pesan:
Program selesai.
Kemudian perulangan dihentikan menggunakan perintah break, sehingga program berhenti dijalankan.

## Link YouTube
https://youtu.be/qRWi_TIkcJI
