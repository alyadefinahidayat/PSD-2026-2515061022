class StackPakaian:
    def __init__(self, max_size=5):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, pakaian):
        if self.is_full():
            print("Tumpukan pakaian penuh")
            return

        self.top_idx += 1
        self.st[self.top_idx] = pakaian
        print(f'Pakaian "{pakaian}" berhasil ditambahkan')

    def pop(self):
        if self.is_empty():
            print("Tumpukan pakaian kosong")
            return

        print(f'Pakaian "{self.st[self.top_idx]}" berhasil diambil')
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Tumpukan pakaian kosong")
            return

        print(f'Pakaian teratas: "{self.st[self.top_idx]}"')

    def display(self):
        if self.is_empty():
            print("Tumpukan pakaian kosong")
            return

        print("Daftar pakaian (atas ke bawah):")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")

    def jumlah_pakaian(self):
        jumlah = self.top_idx + 1
        print(f"Jumlah pakaian dalam tumpukan: {jumlah}")


def main():
    stack = StackPakaian()
    pilih = 0

    while pilih != 6:
        print("\n=== SISTEM TUMPUKAN PAKAIAN ===")
        print("1. Tambah Pakaian")
        print("2. Ambil Pakaian")
        print("3. Lihat Pakaian Teratas")
        print("4. Tampilkan Semua Pakaian")
        print("5. Hitung Jumlah Pakaian")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            pakaian = input("Masukkan nama pakaian: ")
            stack.push(pakaian)

        elif pilih == 2:
            stack.pop()

        elif pilih == 3:
            stack.peek()

        elif pilih == 4:
            stack.display()

        elif pilih == 5:
            stack.jumlah_pakaian()

        elif pilih == 6:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()