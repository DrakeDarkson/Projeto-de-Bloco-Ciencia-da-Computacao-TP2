import time
import numpy as np
from multiprocessing import Pool, cpu_count

def soma_sequencial(lista):
    return sum(lista)

def soma_parcial(args):
    lista, inicio, fim = args
    return sum(lista[inicio:fim])

def soma_paralela(lista, num_threads):
    tamanho = len(lista)
    partes = [(lista, i * (tamanho // num_threads), (i + 1) * (tamanho // num_threads)) for i in range(num_threads)]
    partes[-1] = (lista, partes[-1][1], tamanho)
    
    with Pool(num_threads) as p:
        resultados = p.map(soma_parcial, partes)
    
    return sum(resultados)

lista = np.random.randint(1, 100, 10**6)

inicio = time.time()
soma_seq = soma_sequencial(lista)
fim = time.time()
tempo_seq = fim - inicio

num_threads = cpu_count()
inicio = time.time()
soma_par = soma_paralela(lista, num_threads)
fim = time.time()
tempo_par = fim - inicio

print(f"Soma Sequencial: {soma_seq}, Tempo: {tempo_seq:.6f}s")
print(f"Soma Paralela: {soma_par}, Tempo: {tempo_par:.6f}s com {num_threads} threads")
