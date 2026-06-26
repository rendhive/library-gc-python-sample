import gc

class TestEnvironment:
    def __init__(self):
        self.active = True

    def deactivate(self):
        self.active = False

test_env = TestEnvironment()
gc.collect()  # Menggunakan environment di dalam proses garbage collection
# Fungsi: Menggunakan garbage collector dalam konteks lingkungan teruji.
# Kondisi: Ketika Anda ingin menguji penggunaan dan perilaku memori dalam situasi yang dikendalikan.