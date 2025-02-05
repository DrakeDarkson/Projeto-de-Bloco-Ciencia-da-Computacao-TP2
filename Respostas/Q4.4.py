import itertools
import time

def permutacoes_unicas(s):
    return sorted(set(itertools.permutations(s)))

def main():
    entrada = "abc"
    inicio = time.time()
    resultado = permutacoes_unicas(entrada)
    fim = time.time()
    
    for p in resultado:
        print("".join(p))
    
    print(f"Tempo total de execução: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
