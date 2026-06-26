import gc

class MyClass:
    pass

obj = MyClass()
obj = None  # Menghapus referensi

gc.collect()  # Memicu pengumpulan sampah
print("Objek yang tidak tersambung:")
unreachable_objects = gc.garbage
print(unreachable_objects)  # Mendapatkan objek yang tidak dapat dijangkau
# Fungsi: Mengambil objek yang tidak dapat dijangkau setelah pengumpulan.
# Kondisi: Ketika Anda ingin menganalisis objek yang tidak terpakai.