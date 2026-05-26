# Program Pencarian Data Buku Perpustakaan
# Menggunakan Binary Search Tree (BST)

class Node:
    def __init__(self, judul):
        self.judul = judul
        self.left = None
        self.right = None


class BSTPerpustakaan:
    def __init__(self):
        self.root = None

    # Menambahkan buku
    def insert_node(self, root, judul):
        if root is None:
            return Node(judul)

        if judul.lower() < root.judul.lower():
            root.left = self.insert_node(root.left, judul)

        elif judul.lower() > root.judul.lower():
            root.right = self.insert_node(root.right, judul)

        return root

    def insert(self, judul):
        self.root = self.insert_node(self.root, judul)

    # Mencari buku
    def search_node(self, root, judul):
        if root is None:
            return False

        if root.judul.lower() == judul.lower():
            return True

        if judul.lower() < root.judul.lower():
            return self.search_node(root.left, judul)

        return self.search_node(root.right, judul)

    def search(self, judul):
        return self.search_node(self.root, judul)

    # Menampilkan buku secara urut
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.judul)
        self.inorder(root.right)

    # Menampilkan preorder
    def preorder(self, root):
        if root is None:
            return

        print(root.judul)
        self.preorder(root.left)
        self.preorder(root.right)

    # Menampilkan postorder
    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.judul)

    # Mencari buku pertama (abjad terkecil)
    def find_min(self, root):
        if root is None:
            return "-"

        current = root
        while current.left is not None:
            current = current.left

        return current.judul

    # Mencari buku terakhir (abjad terbesar)
    def find_max(self, root):
        if root is None:
            return "-"

        current = root
        while current.right is not None:
            current = current.right

        return current.judul

    # Menghitung jumlah buku
    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    bst = BSTPerpustakaan()
    pilih = 0

    while pilih != 8:
        print("\n=== PERPUSTAKAAN BST ===")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Tampilkan Inorder")
        print("4. Tampilkan Preorder")
        print("5. Tampilkan Postorder")
        print("6. Buku Awal (Min)")
        print("7. Buku Akhir (Max)")
        print("8. Jumlah Buku")
        print("9. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        # Tambah buku
        if pilih == 1:
            judul = input("Masukkan judul buku: ")
            bst.insert(judul)
            print(f"Buku '{judul}' berhasil ditambahkan")

        # Cari buku
        elif pilih == 2:
            judul = input("Masukkan judul buku yang dicari: ")

            if bst.search(judul):
                print("Buku ditemukan")
            else:
                print("Buku tidak ditemukan")

        # Inorder
        elif pilih == 3:
            print("\nDaftar Buku (Inorder):")
            bst.inorder(bst.root)

        # Preorder
        elif pilih == 4:
            print("\nDaftar Buku (Preorder):")
            bst.preorder(bst.root)

        # Postorder
        elif pilih == 5:
            print("\nDaftar Buku (Postorder):")
            bst.postorder(bst.root)

        # Min
        elif pilih == 6:
            print(f"Buku pertama: {bst.find_min(bst.root)}")

        # Max
        elif pilih == 7:
            print(f"Buku terakhir: {bst.find_max(bst.root)}")

        # Count
        elif pilih == 8:
            print(f"Jumlah buku: {bst.count_nodes(bst.root)}")

        # Keluar
        elif pilih == 9:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()