import multiprocessing
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_balanced_bst(sorted_values):
    if not sorted_values:
        return None
    mid = len(sorted_values) // 2
    root = Node(sorted_values[mid])
    root.left = build_balanced_bst(sorted_values[:mid])
    root.right = build_balanced_bst(sorted_values[mid+1:])
    return root

def search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    return search(node.left, target) or search(node.right, target)

def parallel_search(root, target):
    if root is None:
        return False
    with multiprocessing.Pool(2) as pool:
        left_result, right_result = pool.starmap(search, [(root.left, target), (root.right, target)])
    return left_result or right_result

def measure_time(size):
    values = list(range(1, size + 1))
    root = build_balanced_bst(values)
    target = size // 2
    
    start = time.time()
    search(root, target)
    seq_time = time.time() - start
    
    start = time.time()
    parallel_search(root, target)
    par_time = time.time() - start
    
    return size, seq_time, par_time

sizes = [2**i for i in range(1, 11)]
results = [measure_time(size) for size in sizes]

for size, seq_time, par_time in results:
    print(f"Tamanho: {size}, Sequencial: {seq_time:.6f}s, Paralelo: {par_time:.6f}s")
