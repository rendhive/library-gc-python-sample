import gc

print("Memantau semua objek saat ini:")
for obj in gc.get_objects():
    print(type(obj))
# Fungsi: Melihat jenis masing-masing objek dalam memori.
# Kondisi: Ketika Anda ingin mengaudit penggunaan objek dalam aplikasi.