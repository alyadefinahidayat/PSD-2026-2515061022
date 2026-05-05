# Sistem Mengurutkan Nilai Siswa Menggunakan Algoritma Bubble Sort
## Deskripsi Singkat
Algoritma ini bekerja dengan cara menelusuri data secara berulang dari elemen pertama hingga elemen terakhir, kemudian membandingkan setiap pasangan elemen yang bersebelahan.
## Source Code
<img width="266" height="80" alt="WhatsApp Image 2026-05-05 at 22 32 18" src="https://github.com/user-attachments/assets/80483e5c-104e-4325-a70f-cf9fc564d245" />
Pada baris 1–4, dibuat fungsi tukar() digunakan untuk menukar posisi dua data dalam sebuah list atau array. Fungsi ini bekerja dengan menyimpan sementara salah satu nilai ke dalam variabel temp, kemudian mengganti posisi data pertama dengan data kedua, lalu mengisi posisi data kedua dengan nilai yang sebelumnya disimpan sementara. Proses tersebut dilakukan agar nilai asli tidak hilang saat pertukaran berlangsung. Dengan adanya fungsi ini, proses pengurutan data menjadi lebih mudah karena program dapat memindahkan posisi elemen yang belum sesuai urutannya.

<img width="462" height="97" alt="5da319ea-7f6e-43b4-90fc-e1cd63654624" src="https://github.com/user-attachments/assets/c5a38a6b-5ab4-4367-bfdd-f78dbf81b362" />
Pada baris 7–11, dibuat fungsi bubble_sort() yang digunakan untuk mengurutkan data menggunakan metode Bubble Sort. Fungsi ini bekerja dengan membandingkan dua data yang berdekatan secara berulang, kemudian menukarnya jika urutannya salah. Pada program ini, data yang dibandingkan adalah nilai siswa yang berada pada indeks kedua ([1]) dari setiap elemen list, sehingga proses sorting dilakukan berdasarkan nilai siswa, bukan nama siswa. Perulangan pertama digunakan untuk menentukan jumlah tahap pengurutan, sedangkan perulangan kedua digunakan untuk membandingkan data satu per satu. Jika nilai pada posisi kiri lebih besar daripada nilai di sebelah kanannya, maka fungsi tukar() dipanggil untuk menukar posisi kedua data tersebut. Proses ini terus dilakukan hingga seluruh data berhasil diurutkan dari nilai terkecil ke terbesar.

<img width="511" height="610" alt="118daa87-12c8-4a78-bd5b-95194587c8fa" src="https://github.com/user-attachments/assets/7317ecd8-32d6-4c5d-b99b-f8fbd68cf2b0" />
Pada baris 14–45, dibuat fungsi main() yang berfungsi sebagai program utama untuk menjalankan seluruh proses pengolahan data siswa. Program dimulai dengan meminta pengguna memasukkan jumlah siswa, kemudian menggunakan try-except untuk memastikan input yang diberikan berupa angka. Jika input tidak valid, program akan menampilkan pesan kesalahan dan menghentikan proses. Setelah itu, program membuat list kosong bernama data_siswa yang digunakan untuk menyimpan nama dan nilai siswa.
Selanjutnya, program melakukan perulangan sesuai jumlah siswa untuk memasukkan data setiap siswa. Pada setiap perulangan, pengguna diminta memasukkan nama siswa dan nilai siswa. Input nilai juga menggunakan try-except agar hanya menerima angka, sehingga jika pengguna memasukkan selain angka, program akan meminta input ulang sampai benar. Data yang berhasil dimasukkan kemudian disimpan ke dalam list dalam bentuk [nama, nilai].
Setelah semua data dimasukkan, program menampilkan data siswa sebelum diurutkan. Kemudian fungsi bubble_sort() dipanggil untuk mengurutkan data berdasarkan nilai siswa dari yang terkecil ke terbesar. Setelah proses sorting selesai, program menampilkan kembali data siswa yang sudah terurut. Dengan demikian, fungsi main() mengatur seluruh alur program mulai dari input data, validasi, penyimpanan data, proses sorting, hingga menampilkan hasil akhir.

<img width="287" height="44" alt="c4946643-3805-41a9-84e1-c7d6d1e52c82" src="https://github.com/user-attachments/assets/11e9346c-914e-49f9-9f0d-075d87f402bd" />
Pada baris 48–49, digunakan untuk menentukan apakah file Python dijalankan secara langsung atau tidak. Bagian if __name__ == "__main__": berfungsi sebagai pengecekan utama pada program Python. Jika file dijalankan langsung, maka nilai __name__ akan menjadi "__main__" sehingga fungsi main() akan dipanggil dan program dijalankan. Namun, jika file tersebut dipanggil atau diimpor ke program lain sebagai module, maka fungsi main() tidak akan otomatis dijalankan. Dengan cara ini, program menjadi lebih terstruktur dan aman digunakan kembali pada file lain tanpa langsung mengeksekusi seluruh isi program.

## Output Program
<img width="351" height="362" alt="f89c476b-7eb5-409b-955d-c3e822070055" src="https://github.com/user-attachments/assets/5d8373d5-d0d3-4db9-a430-8666de0b9624" />
Program meminta pengguna untuk memasukan jumlah siswa. Setelah itu pengguna diminta untuk memasukkan nama siswa dan nilai siswa ke 1-5.

<img width="450" height="212" alt="be1e678f-c6cc-4b57-85bb-65c2b59abd65" src="https://github.com/user-attachments/assets/868a671a-4e70-4165-bb1a-498ce80db1d7" />
Selanjutnya, program akan menampilkan data nama siswa dan nilai siswa sebelum urutkan. Serta menampilkan nama siswa dan nilai siswa setelah diurutkan.

## Link YouTube
https://youtu.be/AfqBh1yDpIM
