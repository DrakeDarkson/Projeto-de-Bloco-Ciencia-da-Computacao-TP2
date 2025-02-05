import multiprocessing
import time
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    with multiprocessing.Pool(2) as pool:
        left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    size = 1000000
    arr = [random.randint(0, 1000000) for _ in range(size)]
    seq_time = measure_time(merge_sort, arr[:])
    par_time = measure_time(parallel_merge_sort, arr[:])
    print(f"Tempo Sequencial: {seq_time:.6f} segundos")
    print(f"Tempo Paralelo: {par_time:.6f} segundos")
