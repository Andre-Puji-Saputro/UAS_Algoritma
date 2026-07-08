
# ============ 1. STACK: Riwayat Pemeriksaan ============
class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop() if not self.is_empty() else None

    def peek(self):
        return self.data[-1] if not self.is_empty() else None

    def display(self):
        if self.is_empty():
            print("Riwayat pemeriksaan masih kosong.")
            return
        print("Riwayat Pemeriksaan Terakhir:")
        for id_pasien, nama in reversed(self.data):
            print(f"- ID {id_pasien} | {nama}")


# ============ 2. QUEUE: Antrean Reguler ============
class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0) if not self.is_empty() else None

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def display(self):
        if self.is_empty():
            print("Antrean reguler masih kosong.")
            return
        print("Antrean Reguler:")
        for item in self.data:
            print(f"- {item}")


# ============ 3: Antrean UGD (Prioritas) ============
class MaxHeap:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def insert(self, priority, name):
        self.data.append((priority, name))
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent][0] >= self.data[i][0]:
                break
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def delete_root(self):
        if self.is_empty():
            return None
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return top

    def heapify_down(self, i):
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            largest = i
            if left < n and self.data[left][0] > self.data[largest][0]:
                largest = left
            if right < n and self.data[right][0] > self.data[largest][0]:
                largest = right
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def display(self):
        if self.is_empty():
            print("Antrean UGD masih kosong.")
            return
        print("Antrean UGD (Berdasarkan Tingkat Keparahan):")
        for priority, name in self.data:
            print(f"- [Level {priority}] {name}")


# ============ 4. BST: Rekam Medis Pasien ============
class RekamMedisNode:
    def __init__(self, patient_id, name, diagnosis):
        self.id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, patient_id, name, diagnosis):
        self.root = self._insert(self.root, patient_id, name, diagnosis)

    def _insert(self, node, patient_id, name, diagnosis):
        if node is None:
            return RekamMedisNode(patient_id, name, diagnosis)
        if patient_id < node.id:
            node.left = self._insert(node.left, patient_id, name, diagnosis)
        elif patient_id > node.id:
            node.right = self._insert(node.right, patient_id, name, diagnosis)
        else:
            node.diagnosis = diagnosis 
        return node

    def search(self, patient_id):
        node = self.root
        while node and node.id != patient_id:
            node = node.left if patient_id < node.id else node.right
        return node

    def delete(self, patient_id):
        self.root = self._delete(self.root, patient_id)

    def _delete(self, node, patient_id):
        if node is None:
            return None
        if patient_id < node.id:
            node.left = self._delete(node.left, patient_id)
        elif patient_id > node.id:
            node.right = self._delete(node.right, patient_id)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            pengganti = node.right
            while pengganti.left:
                pengganti = pengganti.left
            node.id, node.name, node.diagnosis = pengganti.id, pengganti.name, pengganti.diagnosis
            node.right = self._delete(node.right, pengganti.id)
        return node

    def inorder(self):
        print("Rekam Medis (urut berdasarkan ID):")
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"ID {node.id} | {node.name} | Diagnosis: {node.diagnosis}")
            self._inorder(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)


# ============ 5. PROGRAM UTAMA (Integrasi Sistem) ============
def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit():
            return int(nilai)
        print("Input harus berupa angka, coba lagi.")


def main():
    antrean_reguler = Queue()
    antrean_ugd = MaxHeap()
    rekam_medis = BST()
    riwayat = Stack()

    menu = """
=== SISTEM MANAJEMEN KLINIK SEHAT ===
1. Daftar Pasien Reguler
2. Daftar Pasien UGD (Prioritas)
3. Panggil Pasien untuk Diperiksa
4. Lihat Semua Antrean
5. Cari Rekam Medis (ID)
6. Lihat Semua Rekam Medis & Info Pohon
7. Hapus Rekam Medis (ID)
8. Lihat Riwayat Pemeriksaan
9. Undo Pemeriksaan Terakhir (Batalkan)
0. Keluar
"""

    while True:
        print(menu)
        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            nama = input("Nama pasien: ")
            antrean_reguler.enqueue(nama)
            print(f"'{nama}' masuk ke antrean reguler.")

        elif pilihan == '2':
            nama = input("Nama pasien UGD: ")
            skala = input_angka("Tingkat keparahan (1-10): ")
            antrean_ugd.insert(skala, nama)
            print(f"'{nama}' masuk UGD dengan tingkat keparahan {skala}.")

        elif pilihan == '3':
            if not antrean_ugd.is_empty():
                prioritas, nama = antrean_ugd.delete_root()
                print(f"\n[URGENT] Memanggil pasien UGD: {nama} (Keparahan: {prioritas})")
            elif not antrean_reguler.is_empty():
                nama = antrean_reguler.dequeue()
                print(f"\nMemanggil pasien reguler: {nama}")
            else:
                print("\nTidak ada pasien dalam antrean.")
                continue

            id_pasien = input_angka(f"ID rekam medis untuk {nama}: ")
            diagnosis = input(f"Diagnosis untuk {nama}: ")
            rekam_medis.insert(id_pasien, nama, diagnosis)
            riwayat.push((id_pasien, nama))
            print(f"Rekam medis '{nama}' berhasil disimpan.")

        elif pilihan == '4':
            print("\n--- STATUS ANTREAN ---")
            antrean_ugd.display()
            if not antrean_ugd.is_empty():
                prioritas, nama = antrean_ugd.peek()
                print(f"Berikutnya dipanggil dari UGD: {nama} - Level {prioritas}")
            antrean_reguler.display()
            if not antrean_reguler.is_empty():
                print(f"Berikutnya dipanggil dari antrean reguler: {antrean_reguler.peek()}")

        elif pilihan == '5':
            cari_id = input_angka("Masukkan ID pasien yang dicari: ")
            hasil = rekam_medis.search(cari_id)
            if hasil:
                print(f"Ditemukan - ID: {hasil.id} | Nama: {hasil.name} | Diagnosis: {hasil.diagnosis}")
            else:
                print("Data pasien tidak ditemukan.")

        elif pilihan == '6':
            print()
            rekam_medis.inorder()
            print(f"\nTotal data: {rekam_medis.count()}")
            print(f"Ketinggian pohon: {rekam_medis.height()}")

        elif pilihan == '7':
            hapus_id = input_angka("Masukkan ID rekam medis yang dihapus: ")
            if rekam_medis.search(hapus_id):
                rekam_medis.delete(hapus_id)
                print("Rekam medis berhasil dihapus.")
            else:
                print("Data pasien tidak ditemukan.")

        elif pilihan == '8':
            print()
            riwayat.display()
            if not riwayat.is_empty():
                id_terakhir, nama_terakhir = riwayat.peek()
                print(f"Pasien terakhir yang diperiksa: {nama_terakhir} (ID {id_terakhir})")

        elif pilihan == '9':
            if riwayat.is_empty():
                print("\nTidak ada riwayat pemeriksaan yang bisa dibatalkan.")
                continue
            id_pasien, nama = riwayat.pop()
            rekam_medis.delete(id_pasien)
            print(f"\nUndo berhasil: pemeriksaan '{nama}' (ID {id_pasien}) dibatalkan,")
            print("dan rekam medisnya sudah dihapus dari BST.")

        elif pilihan == '0':
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()