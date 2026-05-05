def tukar(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def bubble_sort(data, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][1] > data[j + 1][1]:
                tukar(data, j, j + 1)


def main():
    try:
        jumlah = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    data_siswa = []

    for i in range(jumlah):
        print(f"\nData siswa ke-{i+1}")

        nama = input("Masukkan nama siswa: ")

        while True:
            try:
                nilai = int(input("Masukkan nilai siswa: "))
                break
            except ValueError:
                print("Nilai harus berupa angka!")

        data_siswa.append([nama, nilai])

    print("\nData sebelum diurutkan:")
    for siswa in data_siswa:
        print(f"Nama: {siswa[0]}, Nilai: {siswa[1]}")

    bubble_sort(data_siswa, jumlah)

    print("\nData setelah diurutkan berdasarkan nilai:")
    for siswa in data_siswa:
        print(f"Nama: {siswa[0]}, Nilai: {siswa[1]}")


if __name__ == "__main__":
    main()