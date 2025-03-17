import time
import matplotlib.pyplot as plt

def hanoi(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append(f"{origem} -> {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino, movimentos)
    movimentos.append(f"{origem} -> {destino}")
    hanoi(n - 1, auxiliar, destino, origem, movimentos)

def medir_tempo(n):
    movimentos = []
    inicio = time.time()
    hanoi(n, 'A', 'C', 'B', movimentos)
    fim = time.time()
    return fim - inicio, movimentos

discos = list(range(1, 6)) # list(range(1, 31))
tempos = []
todos_movimentos = {}

for n in discos:
    tempo, movimentos = medir_tempo(n)
    tempos.append(tempo)
    todos_movimentos[n] = movimentos

plt.plot(discos, tempos, marker='o')
plt.xlabel('Número de Discos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Complexidade das Torres de Hanói')
plt.grid()
plt.show()

print(todos_movimentos)
