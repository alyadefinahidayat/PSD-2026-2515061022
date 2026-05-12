# Sistem Pencarian Nama Siswa Dalam Absensi

## Deskripsi Singkat
Program ini merupakan implementasi sederhana dari metode Sequential Searching menggunakan bahasa Python. Program digunakan untuk mencari nama siswa dalam sebuah daftar secara berurutan dari data pertama hingga data terakhir. Pengguna diminta memasukkan nama yang ingin dicari, kemudian program akan memeriksa setiap elemen pada list siswa satu per satu. Jika nama ditemukan, program akan menampilkan jumlah kemunculan nama tersebut dalam daftar, sedangkan jika tidak ditemukan program akan menampilkan pesan bahwa nama tidak ada dalam data.

## Source Code
<img width="412" height="171" alt="part1 (1)" src="https://github.com/user-attachments/assets/7dcc7e5e-4a21-4a3d-99b0-c19ba0c12739" />

Bagian program tersebut merupakan fungsi sequential_search yang digunakan untuk melakukan pencarian data secara berurutan atau sequential searching. Fungsi ini memiliki dua parameter, yaitu data sebagai daftar data yang akan dicari dan target sebagai data yang ingin ditemukan. Variabel ditemukan diinisialisasi dengan nilai 0 untuk menghitung jumlah kemunculan data yang dicari. Selanjutnya, program menggunakan perulangan for untuk memeriksa setiap elemen dalam list data mulai dari indeks pertama hingga terakhir. Pada setiap perulangan, program membandingkan isi data dengan target menggunakan method .lower() agar pencarian tidak membedakan huruf besar dan kecil. Jika data yang diperiksa sama dengan target, maka nilai ditemukan akan bertambah satu. Setelah seluruh data selesai diperiksa, fungsi akan mengembalikan nilai ditemukan sebagai hasil jumlah data yang berhasil ditemukan.

<img width="655" height="296" alt="2a467589-fd81-4662-a7c1-52b1eae87648" src="https://github.com/user-attachments/assets/25164116-eb4c-4cd9-b0a1-d1970fb1fc93" />

Bagian program tersebut merupakan fungsi utama main() yang digunakan untuk menjalankan keseluruhan proses pencarian data. Pada awal fungsi, dibuat sebuah list bernama siswa yang berisi beberapa nama siswa. Setelah itu, program menampilkan daftar nama siswa menggunakan perintah print(). Selanjutnya, pengguna diminta memasukkan nama siswa yang ingin dicari melalui fungsi input(), lalu input tersebut disimpan ke dalam variabel target. Program kemudian memanggil fungsi sequential_search(siswa, target) untuk melakukan proses pencarian nama secara berurutan dalam list siswa, dan hasil pencarian disimpan pada variabel hasil. Jika nilai hasil lebih dari 0, maka program akan menampilkan pesan bahwa nama tersebut ditemukan beserta jumlah kemunculannya. Namun, jika nilai hasil sama dengan 0, program akan menampilkan pesan bahwa nama yang dicari tidak ditemukan. Pada bagian akhir, terdapat kondisi if __name__ == "__main__": yang berfungsi untuk memastikan bahwa fungsi main() dijalankan saat file program dieksekusi secara langsung.

## 0utput Program
<img width="639" height="64" alt="1c40d2e8-680a-48cb-813c-a49dfe227237" src="https://github.com/user-attachments/assets/ac3a80d6-3cbf-4f77-91e5-82b95a8e085a" />

Bagian output program tersebut menunjukkan hasil dari proses pencarian menggunakan metode Sequential Searching. Awalnya, program menampilkan daftar nama siswa yang tersimpan dalam list, yaitu ['aya', 'rara', 'call', 'bunan', 'shin', 'kia', 'nur', 'call', 'bunan']. Setelah itu, pengguna memasukkan nama yang ingin dicari, yaitu “bunan”. Program kemudian melakukan pencarian secara berurutan dari data pertama hingga terakhir untuk memeriksa apakah nama tersebut terdapat dalam daftar. Hasil pencarian menunjukkan bahwa nama “bunan” ditemukan sebanyak 2 kali, karena nama tersebut muncul pada dua posisi berbeda di dalam list siswa.

## Link YouTube
https://youtu.be/Fe5GAnzz4ds

## Tugas Akhir Tulis Tangan
<img width="1023" height="1600" alt="1d2b223b-9712-4ebd-87cf-a898e1409305" src="https://github.com/user-attachments/assets/ead15009-df45-41d7-927e-a4a66ac1b778" />
