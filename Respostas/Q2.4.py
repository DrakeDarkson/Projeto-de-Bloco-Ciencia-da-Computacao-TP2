import random
import time

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

def find_median(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr, n // 2)
    else:
        return (quickselect(arr, n // 2 - 1) + quickselect(arr, n // 2)) / 2

def find_k_smallest(arr, k):
    threshold = quickselect(arr, k - 1)
    return [x for x in arr if x <= threshold][:k]

def main():
    arr = [random.randint(1, 1000) for _ in range(10000)]
    start_time = time.time()
    median = find_median(arr)
    k_smallest = find_k_smallest(arr, 10)
    end_time = time.time()
    print(f"Mediana: {median}")
    print(f"10 menores elementos: {k_smallest}")
    print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
