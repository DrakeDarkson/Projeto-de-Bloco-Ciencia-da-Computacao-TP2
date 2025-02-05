import multiprocessing
import time
import random

def find_max_sequential(arr):
    return max(arr)

def find_max_parallel(arr, num_workers=4):
    chunk_size = len(arr) // num_workers
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers)]
    
    with multiprocessing.Pool(num_workers) as pool:
        local_maxima = pool.map(max, chunks)
    
    return max(local_maxima)

def measure_time(func, arr):
    start = time.time()
    result = func(arr)
    end = time.time()
    print(f"{func.__name__} result: {result}, time: {end - start:.6f} sec")

if __name__ == "__main__":
    size = 10**6
    arr = [random.randint(0, 1000000) for _ in range(size)]
    
    measure_time(find_max_sequential, arr[:])
    measure_time(find_max_parallel, arr[:])
