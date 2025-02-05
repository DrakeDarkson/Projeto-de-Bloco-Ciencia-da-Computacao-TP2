import random
import time

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

def main():
    num_tests = 10
    k_values = [10, 50, 100, 500, 1000]
    for i in range(num_tests):
        arr = [random.randint(1, 1000) for _ in range(10000)]
        print(f"Lista {i+1}:")
        start_time = time.time()
        for k in k_values:
            kth_element = quickselect(arr, k)
            print(f"{k}-ésimo menor elemento: {kth_element}")
        end_time = time.time()
        print(f"Tempo total de execução: {end_time - start_time:.6f} segundos\n")

if __name__ == "__main__":
    main()
