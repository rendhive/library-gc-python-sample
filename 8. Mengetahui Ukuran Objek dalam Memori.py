import gc
import sys

class MyClass:
    pass

obj = MyClass()
print(f"Ukuran objek: {sys.getsizeof(obj)} bytes")
# Fungsi: Mengukur ukuran objek di memori.
# Kondisi: Ketika Anda perlu memantau penggunaan memori dari objek tertentu.