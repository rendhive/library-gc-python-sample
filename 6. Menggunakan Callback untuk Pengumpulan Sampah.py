import gc

def collector_callback(phase, info):
    print(f"Pengumpulan sampah fase: {phase}, Informasi: {info}")

gc.callbacks.append(collector_callback)
gc.collect()  # Memicu pengumpulan untuk melihat callback
# Fungsi: Menambahkan callback untuk menangkap informasi saat pengumpulan sampah.
# Kondisi: Ketika Anda ingin melakukan logging atau analisis ketika garbage collector beroperasi.