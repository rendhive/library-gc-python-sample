import gc

class Node:
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node1.next = node2
node2.next = node1  # Siklus

print("Mencetak objek sebelum pengumpulan:")
gc.collect()  # Memicu pengumpulan
# Fungsi: Menangani objek dengan siklus referensi yang sulit dihapus.
# Kondisi: Ketika Anda ingin memastikan pengumpulan yang efisien walau ada siklus.