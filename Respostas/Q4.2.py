import time
from functools import lru_cache

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

def main():
    n = 30
    fib_rec, time_rec = measure_time(fibonacci_recursive, n)
    fib_memo, time_memo = measure_time(fibonacci_memoized, n)
    
    print(f"Fibonacci recursivo ({n}): {fib_rec}, Tempo: {time_rec:.6f} segundos")
    print(f"Fibonacci com memorização ({n}): {fib_memo}, Tempo: {time_memo:.6f} segundos")

if __name__ == "__main__":
    main()
