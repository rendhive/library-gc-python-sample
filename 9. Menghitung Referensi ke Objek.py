import gc

class MyClass:
    pass

obj = MyClass()
print(f"Jumlah referensi objek sebelum: {gc.get_referrers(obj)}")
obj = None  # Hapus referensi
gc.collect()  # Memicu pengumpulan
print("Jumlah referensi objek setelah: ", gc.get_referrers(obj))
# Fungsi: Menghitung referensi yang ada ke objek tertentu.
# Kondisi: Ketika Anda ingin mengetahui ketergantungan objek.