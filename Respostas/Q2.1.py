import random
import time
import sys

sys.setrecursionlimit(20000)

def quicksort(arr, pivot_type='first'):
    if len(arr) <= 1:
        return arr
    if pivot_type == 'first':
        pivot = arr[0]
    elif pivot_type == 'last':
        pivot = arr[-1]
    elif pivot_type == 'median':
        pivot = arr[len(arr) // 2]
    else:
        raise ValueError("Pivot type must be 'first', 'last', or 'median'")
    
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    left_sorted = quicksort(left, pivot_type)
    right_sorted = quicksort(right, pivot_type)
    
    return left_sorted + [pivot] + right_sorted

def measure_time(arr, pivot_type='first'):
    start_time = time.perf_counter()
    quicksort(arr, pivot_type)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    arr = random.sample(range(1, 10001), 10000)
    
    first_pivot_time = measure_time(arr, 'first')
    last_pivot_time = measure_time(arr, 'last')
    median_pivot_time = measure_time(arr, 'median')

    print(f"Time with first pivot: {first_pivot_time:.4f} seconds")
    print(f"Time with last pivot: {last_pivot_time:.4f} seconds")
    print(f"Time with median pivot: {median_pivot_time:.4f} seconds")

if __name__ == "__main__":
    main()
