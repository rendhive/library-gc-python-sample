import gc

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
print("Debugging diaktifkan untuk objek yang tidak dapat dikumpulkan.")
# Fungsi: Mengaktifkan debugging untuk menemukan objek yang tidak dapat dijangkau.
# Kondisi: Ketika Anda perlu menyelidiki objek yang menyebabkan kebocoran.