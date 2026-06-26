import gc

gc.disable()  # Menonaktifkan garbage collector sementara
print("Garbage collector dinonaktifkan.")
# Fungsi: Menonaktifkan kolektor untuk konteks kritis.
# Kondisi: Ketika Anda tidak ingin intervensi pengumpulan saat melakukan operasi kritis.