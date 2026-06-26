import gc

before_collect = gc.get_stats()  # Informasi sebelum pengumpulan
gc.collect()  # Memicu pengumpulan
after_collect = gc.get_stats()  # Informasi setelah pengumpulan
diff = after_collect - before_collect
print(f"Penggunaan memori berubah: {diff}")
# Fungsi: Mengawasi penggunaan memori dan dampak dari pengumpulan.
# Kondisi: Ketika Anda ingin menganalisis dampak pengumpulan terhadap memori.