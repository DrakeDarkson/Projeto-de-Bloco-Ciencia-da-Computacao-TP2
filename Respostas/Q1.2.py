import random
import time
from cython.parallel import parallel, prange

def sequential_sum(data):
    total = 0
    for value in data:
        total += value
    return total

def parallel_sum(data):
    total = 0
    with parallel():
        for i in prange(len(data), nogil=True):
            total += data[i]
    return total

def main():
    data = [random.randint(1, 100000) for _ in range(10000)]

    start_time = time.perf_counter()
    sequential_result = sequential_sum(data)
    sequential_end_time = time.perf_counter()
    
    parallel_start_time = time.perf_counter()
    parallel_result = parallel_sum(data)
    parallel_end_time = time.perf_counter()

    print(f"Resultado sequencial: {sequential_result}")
    print(f"Resultado paralelo: {parallel_result}")
    print(f"Tempo de execução sequencial: {sequential_end_time - start_time:.4f} segundos")
    print(f"Tempo de execução paralelo: {parallel_end_time - parallel_start_time:.4f} segundos")
    print(f"Tempo total de execução: {parallel_end_time - start_time:.4f} segundos")

if __name__ == "__main__":
    main()
