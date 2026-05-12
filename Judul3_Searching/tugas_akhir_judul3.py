def sequential_search(data, target):
    ditemukan = 0

    for i in range(len(data)):
        if data[i].lower() == target.lower():
            ditemukan += 1

    return ditemukan


def main():
    siswa = ["aya", "rara", "call", "bunan", "shin", "kia","nur","call","bunan"]
    print("Daftar Nama Siswa:", siswa)

    target = input("Masukkan nama siswa yang ingin dicari: ")
    hasil = sequential_search(siswa, target)

    if hasil > 0:
        print(f"Nama {target} ditemukan sebanyak {hasil} kali.")
    else:
        print(f"Nama {target} tidak ditemukan.")


if __name__ == "__main__":
    main()