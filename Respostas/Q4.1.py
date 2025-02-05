import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    test_values = [5, 7, 10, 12, 15]
    start_time = time.time()
    results = {n: factorial(n) for n in test_values}
    end_time = time.time()
    
    for n, fact in results.items():
        print(f"Fatorial de {n}: {fact}")
    
    print(f"Tempo total de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
