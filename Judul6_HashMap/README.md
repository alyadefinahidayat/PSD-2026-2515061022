# Sistem Parkir Kendaraan

## Deskripsi Singkat

Program sistem parkir ini menerapkan struktur data Hash Map Open Addressing dengan metode Linear Probing untuk menyimpan dan mengelola data kendaraan yang masuk ke area parkir. Setiap kendaraan memiliki nomor plat sebagai key dan nama pemilik sebagai value.

## Source Code

Class SlotState berfungsi untuk mendefinisikan status dari setiap slot pada tabel hash. Terdapat tiga kondisi yang dapat dimiliki sebuah slot, yaitu EMPTY yang menunjukkan bahwa slot masih kosong, OCCUPIED yang menunjukkan bahwa slot sedang digunakan untuk menyimpan data kendaraan, dan DELETED yang menunjukkan bahwa data pada slot tersebut telah dihapus. Penggunaan status DELETED sangat penting dalam metode Open Addressing karena memungkinkan proses pencarian tetap berjalan dengan benar meskipun terdapat data yang telah dihapus sebelumnya.

Class Entry digunakan untuk merepresentasikan satu slot pada tabel hash. Setiap objek Entry memiliki atribut plat untuk menyimpan nomor plat kendaraan, pemilik untuk menyimpan nama pemilik kendaraan, dan state untuk menyimpan status slot. Saat pertama kali dibuat, setiap slot memiliki nilai plat dan pemilik berupa None serta status EMPTY yang menandakan bahwa slot tersebut belum digunakan.

Fungsi init() pada class SistemParkir berfungsi sebagai konstruktor yang digunakan untuk membuat tabel hash dengan ukuran tertentu. Pada saat objek dibuat, sistem akan menginisialisasi sejumlah slot sesuai ukuran yang ditentukan dan mengisi seluruh slot tersebut dengan objek Entry yang masih kosong. Dengan demikian, tabel hash telah siap digunakan untuk menyimpan data kendaraan.

Fungsi hash_function() digunakan untuk menghitung indeks penyimpanan kendaraan pada tabel hash. Fungsi ini bekerja dengan menjumlahkan nilai ASCII dari setiap karakter pada nomor plat kendaraan menggunakan fungsi ord(), kemudian hasilnya dibagi dengan ukuran tabel menggunakan operator modulo (%). Hasil perhitungan tersebut akan menghasilkan indeks yang berada dalam rentang ukuran tabel sehingga dapat digunakan sebagai lokasi penyimpanan data kendaraan.

Fungsi parkir() digunakan untuk menambahkan kendaraan ke dalam sistem parkir. Pertama, sistem menghitung indeks awal menggunakan fungsi hash. Jika slot pada indeks tersebut masih kosong, data kendaraan langsung disimpan. Namun jika slot tersebut sudah terisi oleh kendaraan lain, terjadi collision sehingga sistem akan melakukan Linear Probing, yaitu memeriksa slot berikutnya secara berurutan hingga menemukan slot kosong atau slot yang berstatus DELETED. Setelah menemukan lokasi yang tersedia, data kendaraan akan disimpan dan status slot diubah menjadi OCCUPIED.

Fungsi cari_kendaraan() digunakan untuk mencari data kendaraan berdasarkan nomor plat. Proses pencarian dimulai dengan menghitung indeks hash dari nomor plat yang dicari. Jika kendaraan tidak ditemukan pada indeks awal, sistem akan melakukan Linear Probing dengan memeriksa slot-slot berikutnya sesuai urutan penyisipan data. Jika data ditemukan, fungsi akan mengembalikan objek kendaraan tersebut. Sebaliknya, jika pencarian mencapai slot yang berstatus EMPTY, sistem menyimpulkan bahwa kendaraan tidak terdapat dalam tabel hash.

Fungsi keluar() digunakan untuk menghapus data kendaraan yang keluar dari area parkir. Fungsi ini terlebih dahulu mencari kendaraan menggunakan fungsi pencarian. Jika kendaraan ditemukan, status slot tidak langsung diubah menjadi EMPTY, melainkan menjadi DELETED. Cara ini digunakan agar jalur pencarian (probing sequence) tetap terjaga sehingga kendaraan lain yang berada pada rangkaian probing yang sama masih dapat ditemukan dengan benar.

Fungsi tampilkan_parkir() berfungsi untuk menampilkan seluruh isi tabel hash beserta status setiap slot. Slot yang belum pernah digunakan akan ditampilkan sebagai KOSONG, slot yang datanya telah dihapus ditampilkan sebagai KELUAR, sedangkan slot yang berisi data kendaraan akan menampilkan nomor plat dan nama pemilik kendaraan. Fungsi ini membantu pengguna dalam memantau kondisi area parkir secara keseluruhan.

## Output Program

Output tersebut menunjukkan bahwa program berhasil menyimpan tiga kendaraan ke dalam hash table, yaitu BE1234AA milik Andi pada slot 7, BE5678BB milik Budi pada slot 5, dan BE9999CC milik Citra pada slot 8. Setelah data ditampilkan, program melakukan pencarian terhadap kendaraan BE5678BB dan berhasil menemukan data beserta nama pemiliknya. Selanjutnya, kendaraan tersebut dikeluarkan dari parkiran sehingga status slot 5 berubah menjadi KELUAR (DELETED). Pada tampilan akhir, kendaraan milik Andi dan Citra masih tersimpan di slot masing-masing, sedangkan slot 5 ditandai sebagai KELUAR untuk menjaga proses pencarian tetap berjalan dengan benar sesuai konsep Hash Map Open Addressing menggunakan Linear Probing.

## Link YouTube
