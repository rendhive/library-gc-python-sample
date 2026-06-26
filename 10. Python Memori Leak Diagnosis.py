import gc

class MyClass:
    def __init__(self):
        self.data = "Data besar" * 1000

obj = MyClass()
print("Sebelum memicu pengumpulan:")
gc.collect()
print("Pengumpulan sampah dilakukan.")
# Fungsi: Memicu pengumpulan secara eksplisit dan melihat dampaknya.
# Kondisi: Ketika Anda mencurigai adanya kebocoran memori.