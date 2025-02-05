import random
import time

class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __repr__(self):
        return f"{self.nome}: {self.nota}"

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x.nota < pivot.nota]
    middle = [x for x in lista if x.nota == pivot.nota]
    right = [x for x in lista if x.nota > pivot.nota]
    return quicksort(left) + middle + quicksort(right)

def main():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João"]
    estudantes = [Estudante(random.choice(nomes), random.randint(0, 100)) for _ in range(10)]
    
    print("Lista antes da ordenação:")
    print(estudantes)
    
    start_time = time.perf_counter()
    estudantes_ordenados = quicksort(estudantes)
    end_time = time.perf_counter()
    
    print("\nLista após a ordenação:")
    print(estudantes_ordenados)
    
    print(f"\nTempo total de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
