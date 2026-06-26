import gc

gc.collect()  # Pastikan pengumpulan sampah terjadi
objects = gc.get_objects()
print(f"Jumlah objek aktif dalam memori: {len(objects)}")
# Fungsi: Mengambil daftar objek yang saat ini aktif di memori.
# Kondisi: Ketika Anda ingin melihat berapa banyak objek yang sedang digunakan.