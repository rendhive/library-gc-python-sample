import gc

class MyClass:
    pass

obj = MyClass()
print(f"Objek sebelum pengumpulan: {gc.get_objects()}")
gc.collect()  # Memicu pengumpulan
print(f"Objek setelah pengumpulan: {gc.get_objects()}")
# Fungsi: Memberikan pandangan terdahulu dan setelah dari pengumpulan objek.
# Kondisi: Ketika Anda ingin melihat perubahan sebelum dan sesudah pengumpulan.