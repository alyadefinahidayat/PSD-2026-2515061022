# Sistem Pencarian Data pada Perpustakaan 

## Deskripsi Singkat
Program ini merupakan implementasi sederhana dari metode Binary Search Tree (BST) dengan bahasa Python. Program dapat digunakan untuk menambah, mencari, menampilkan daftar buku, mencari buku pertama dan terakhir berdasarkan alfabet, serta menghitung jumlah buku.

## Source Code
<img width="268" height="97" alt="c4f5853e-7a6f-4a6c-8ca9-f18d49e74af4" src="https://github.com/user-attachments/assets/7abbf088-f9ce-4cc4-8379-6811584c122f" />

Bagian program tersebut merupakan Class Node yang digunakan untuk membuat node atau simpul pada Binary Search Tree (BST). Dimana setiap node menyimpan satu data berupa judul buku. Variabel self.left digunakan untuk menyimpan anak kiri, sedangkan self.right digunakan untuk menyimpan anak kanan. Nilai awal keduanya adalah None karena node baru belum memiliki cabang.

<img width="239" height="76" alt="WhatsApp Image 2026-05-26 at 21 11 59" src="https://github.com/user-attachments/assets/c0734b26-aa50-477c-9b14-7abdb0bd0cb5" />

Bagian program tersebut merupakan Class BSTPerpustakaan yang digunakan untuk mengelola seluruh operasi BST. Pada fungsi __init__, dibuat variabel self.root yang berfungsi sebagai akar pohon BST. Nilainya None karena saat program dimulai belum ada data buku.

<img width="514" height="215" alt="ss ta 5,2" src="https://github.com/user-attachments/assets/e7577ccf-7f7b-441a-927d-cd55d58aa340" />

Bagian program tersebut merupakan Fungsi insert_node() yang digunakan untuk menambahkan buku ke dalam BST secara rekursif. Jika node kosong, maka dibuat node baru menggunakan Node(judul). Jika judul lebih kecil dari node saat ini, data dimasukkan ke subtree kiri. Jika lebih besar, data dimasukkan ke subtree kanan. Fungsi lower() digunakan agar perbandingan huruf besar dan kecil tidak memengaruhi proses.

<img width="401" height="59" alt="ss ta 5,4" src="https://github.com/user-attachments/assets/8e595735-daaa-4190-bd5b-b8ee467640b7" />

Bagian program tersebut merupakan Fungsi insert() yang digunakan untuk mempermudah pemanggilan fungsi insert_node(). Fungsi ini menerima judul buku lalu memasukkannya ke BST melalui root.

<img width="412" height="219" alt="ss ta 5,5 (1)" src="https://github.com/user-attachments/assets/aa2448b3-7b75-44a5-bc08-754a334aaf3e" />

Bagian program tersebut merupakan Fungsi search_node() yang digunakan untuk mencari data buku di dalam BST secara rekursif. Jika node kosong, berarti buku tidak ditemukan sehingga fungsi mengembalikan False. Jika judul sama dengan node saat ini, fungsi mengembalikan True. Jika judul lebih kecil maka pencarian dilakukan ke kiri, sedangkan jika lebih besar pencarian dilakukan ke kanan.

<img width="392" height="202" alt="ss ta 5,6" src="https://github.com/user-attachments/assets/d5ebe2bd-1646-43cd-960e-7143c9498668" />

Bagian program tersebut merupakan Fungsi search() yang digunakan untuk mempermudah proses pencarian buku. Fungsi ini memanggil search_node() dengan parameter root BST. 
Sedangkan Fungsi inorder() digunakan untuk menampilkan data buku dengan traversal inorder, yaitu kiri → root → kanan. Karena BST menyimpan data secara terurut, hasil traversal inorder akan menampilkan judul buku berdasarkan urutan alfabet.

<img width="301" height="298" alt="092d64d0-fd02-4c88-8093-2045cbc08cf1" src="https://github.com/user-attachments/assets/9ad28572-44b8-482a-bb38-b12df607f1ed" />

Bagian program tersebut merupakan Fungsi preorder() yang digunakan untuk traversal preorder dengan urutan root → kiri → kanan. Node induk ditampilkan terlebih dahulu sebelum anak kiri dan kanan. Sedangkan Fungsi postorder() digunakan untuk traversal postorder dengan urutan kiri → kanan → root. Pada metode ini node induk ditampilkan terakhir.

<img width="346" height="372" alt="7d0ab0cb-7dd4-41fb-8e08-38966dda0a66" src="https://github.com/user-attachments/assets/df59694a-e9e6-4d6d-bdb0-f62acc956586" />

Bagian program tersebut merupakan Fungsi find_min() yang digunakan untuk mencari judul buku paling awal berdasarkan alfabet. Dalam BST, data terkecil selalu berada di cabang kiri paling ujung. Fungsi akan terus bergerak ke kiri hingga mencapai node terakhir. Sedangkan Fungsi find_max() digunakan untuk mencari judul buku paling akhir berdasarkan alfabet. Pada BST, data terbesar berada di cabang kanan paling ujung.

<img width="682" height="91" alt="dc737fd9-8c78-4f0d-b571-702c77f86c95" src="https://github.com/user-attachments/assets/41016a79-8184-4eec-87cb-446d9e0a5cf7" />

Bagian program tersebut merupakan Fungsi count_nodes() digunakan untuk menghitung jumlah seluruh node atau buku dalam BST. Fungsi bekerja secara rekursif dengan menjumlahkan node saat ini, subtree kiri, dan subtree kanan.

<img width="410" height="403" alt="3006da5a-6955-417a-9c30-8f6262242ff1" src="https://github.com/user-attachments/assets/7b38fe98-bdf2-4c26-ad2d-debcf6f45fea" />

Bagian program tersebut merupakan Fungsi main() yaitu fungsi utama program. Di dalamnya dibuat objek BST bernama bst dan variabel pilih untuk menyimpan pilihan menu pengguna. Pada bagian perulangan while digunakan untuk menampilkan menu program secara berulang. Dimana pengguna dapat memilih menu sesuai kebutuhan seperti menambah buku, mencari buku, melihat traversal, hingga keluar program. Sedangkan try-except digunakan untuk menangani kesalahan jika pengguna memasukkan selain angka.

<img width="485" height="86" alt="ss ta 5,7" src="https://github.com/user-attachments/assets/f8f6800e-5bc7-4ec7-8a42-2526677da81a" />

Bagian ini digunakan untuk menambahkan buku ke BST. Pengguna memasukkan judul buku, kemudian fungsi insert() dipanggil untuk menyimpan data.

<img width="500" height="144" alt="ss ta 5,8" src="https://github.com/user-attachments/assets/a7fd168c-d7c0-4de6-97a6-197dfa9c765e" />

Kode ini digunakan untuk mencari buku berdasarkan judul. Jika fungsi search() mengembalikan True, maka buku ditemukan. Jika False, buku tidak ditemukan.

<img width="317" height="77" alt="ss ta 5,9" src="https://github.com/user-attachments/assets/15b9f81f-5909-4e8e-8bf6-1908e3459c14" />

Bagian ini digunakan untuk menampilkan daftar buku secara inorder sehingga hasilnya terurut berdasarkan alfabet.

<img width="429" height="146" alt="579e517c-98c0-436c-a228-970e9f9329f9" src="https://github.com/user-attachments/assets/1cea09e4-11b9-455b-86a6-c48510371a4c" />

Bagian elif pilih == 4: digunakan untuk menampilkan traversal preorder BST. Sedangkan bagian elif pilih == 5: digunakan untuk menampilkan traversal postorder BST.

<img width="543" height="528" alt="ss ta 5,11" src="https://github.com/user-attachments/assets/6331857f-54ea-4652-a471-ed5f2d63fef5" />

Bagian elif pilih == 6: digunakan untuk menampilkan judul buku dengan urutan alfabet paling awal. Lalu bagian elif pilih == 7: digunakan untuk menampilkan judul buku dengan urutan alfabet paling akhir. Selanjutnya bagian elif pilih == 8: digunakan untuk menghitung dan menampilkan jumlah seluruh buku yang tersimpan di BST. Terakhir bagian elif pilih == 9: digunakan untuk mengakhiri program ketika pengguna memilih menu keluar.

<img width="281" height="58" alt="ss ta 5,12" src="https://github.com/user-attachments/assets/ad2397b3-8b6c-4eab-85d0-bff126a2cd0d" />

Bagian ini digunakan untuk menjalankan fungsi main() ketika file Python dieksekusi secara langsung.


## Output Program

<img width="367" height="470" alt="c4fcab01-36ae-4ffe-81b1-41486b6e4e72" src="https://github.com/user-attachments/assets/d1b699b2-39d9-4c10-baf6-5618cb878f79" />

<img width="370" height="488" alt="abe88907-1406-4948-b7af-038463b74ac4" src="https://github.com/user-attachments/assets/5da41408-187c-4685-b07b-8c2a19067e55" />

<img width="425" height="241" alt="a643dcec-0aca-401a-87d9-ade89eb79f1e" src="https://github.com/user-attachments/assets/06ee5207-63d0-478f-b6aa-a44745902999" />

Disini program akan meminta input pengguna, dimana saya telah memasukkan 5 judul buku yang berbeda dengan memilih menu 1 sebanyak 5 kali.

<img width="410" height="229" alt="8311a7cb-aaa3-4618-bcc1-e97f201d767f" src="https://github.com/user-attachments/assets/6498d50f-ff3d-48af-be1c-53de8943b98a" />

Selanjutnya disini saya memasukan pilihan menu yaitu 2 dan saya mencari buku "dongeng putri salju". Karena buku tersebut ada maka "Buku Ditemukan".

<img width="208" height="334" alt="31d942cc-1cb3-4650-9495-85f77a5851aa" src="https://github.com/user-attachments/assets/5d5f8c16-3af0-4cfd-b721-4e3d5920b07c" />

<img width="208" height="304" alt="655943ce-1cdd-4850-81d5-6db06725908d" src="https://github.com/user-attachments/assets/3f9d3bf5-5111-450f-9a69-55aac6bf9872" />

<img width="247" height="327" alt="b8e00ce5-3482-4c7c-bc2a-73792f301fb1" src="https://github.com/user-attachments/assets/1ba61523-8d20-4736-9664-721d61e42a8e" />

Kemudian jika saya memilih menu 3 output yang keluar ada daftar buku(inorder), sedangkan jika saya memilih menu 4 output yang keluar adalah daftar buku(preorder), dan jika saya memilih menu 5 yang keluar adalah daftar menu(postorder).

<img width="283" height="202" alt="e100395c-87bf-4bea-b63b-3b1928fc1aab" src="https://github.com/user-attachments/assets/2348b875-25f9-4ac8-8a47-7a5fc5b46770" />

<img width="295" height="229" alt="3c4fca38-4490-47b3-9229-c734af318fa6" src="https://github.com/user-attachments/assets/a3799ca6-9c72-4936-9891-7841f1015cef" />

<img width="226" height="200" alt="ce8c7196-c5fb-478a-b792-423e8d9cdd89" src="https://github.com/user-attachments/assets/bdb3d183-356b-4198-8c3e-23b59389c30a" />

Selanjutnya disini jika kita memilih menu 6 maka akan keluar buku pertama, sedangkan jika kita memilih menu 7 output yang akan keluar ada buku terakhir. dan yang terakhir jika kita memilih menu 8 yang akan keluar adalah jumlah buku.

## Link Youtube

https://youtu.be/Nr4SrBEQxt8

