import gc

class Node:
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node1.next = node2
node2.next = node1  # Menciptakan siklus

# Melihat objek dalam siklus referensi
uncoll_obj = gc.garbage
print("Objek tidak terkollect:")
print(uncoll_obj)