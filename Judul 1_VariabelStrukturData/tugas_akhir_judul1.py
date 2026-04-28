class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None

class PlaylistQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def tambah_lagu(self, lagu):
        node_baru = Node(lagu)

        if self.rear is None:
            self.front = node_baru
            self.rear = node_baru
        else:
            self.rear.next = node_baru
            self.rear = node_baru

        print(f"Lagu '{lagu}' berhasil ditambahkan ke playlist.")

    def putar_lagu(self):
        if self.front is None:
            print("Playlist kosong.")
            return

        lagu = self.front.lagu
        print(f"Sedang memutar: {lagu}")

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def tampilkan_playlist(self):
        if self.front is None:
            print("Playlist masih kosong.")
            return

        current = self.front
        nomor = 1

        print("===== DAFTAR PLAYLIST =====")

        while current is not None:
            print(f"{nomor}. {current.lagu}")
            current = current.next
            nomor += 1

        print()


playlist = PlaylistQueue()


while True:
    print("===== PROGRAM ANTRIAN PLAYLIST MUSIK =====")
    print("1. Tambah Lagu")
    print("2. Putar Lagu")
    print("3. Tampilkan Playlist")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        lagu = input("Masukkan judul lagu: ")
        playlist.tambah_lagu(lagu)

    elif pilihan == "2":
        playlist.putar_lagu()

    elif pilihan == "3":
        playlist.tampilkan_playlist()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")