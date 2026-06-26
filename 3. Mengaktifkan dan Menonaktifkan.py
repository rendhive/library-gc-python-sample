import gc

gc.disable()  # Menonaktifkan garbage collector
print("Pengumpulan sampah dinonaktifkan.")
print("Status:", gc.isenabled())

gc.enable()  # Mengaktifkan kembali garbage collector
print("Pengumpulan sampah diaktifkan.")
print("Status:", gc.isenabled())
# Fungsi: Mengaktifkan atau menonaktifkan pengumpulan sampah.
# Kondisi: Ketika Anda perlu mengontrol pengumpulan sampah untuk perbaikan performa.