import time
import matplotlib.pyplot as plt

def hanoi(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append((origem, destino))
        return
    hanoi(n - 1, origem, auxiliar, destino, movimentos)
    movimentos.append((origem, destino))
    hanoi(n - 1, auxiliar, destino, origem, movimentos)

def medir_tempo(n):
    movimentos = []
    inicio = time.time()
    hanoi(n, 'A', 'C', 'B', movimentos)
    fim = time.time()
    return fim - inicio

discos = list(range(1, 31))
tempos = [medir_tempo(n) for n in discos]

plt.plot(discos, tempos, marker='o')
plt.xlabel('Número de Discos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Complexidade das Torres de Hanói')
plt.grid()
plt.show()

print("Tempo total de execução para cada valor de n impresso no gráfico.")
