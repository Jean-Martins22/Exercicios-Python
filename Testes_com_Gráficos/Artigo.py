import time
import matplotlib.pyplot as plt

# Bubble Sort


def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    movimentos = 0
    troca = True
    while troca:
        troca = False
        for i in range(n-1):
            comparacoes += 1
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                troca = True
                movimentos += 1
    return comparacoes, movimentos

# Selection Sort


def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    movimentos = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        movimentos += 1
    return comparacoes, movimentos

# Insertion Sort


def insertion_sort(lista):
    n = len(lista)
    comparacoes = 0
    movimentos = 0
    for i in range(1, n):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            comparacoes += 1
            lista[j+1] = lista[j]
            j -= 1
            movimentos += 1
        lista[j+1] = key
        movimentos += 1
    return comparacoes, movimentos


def calcular_tempo_e_contagem(metodo, lista, nome):
    inicio = time.time()
    comparacoes, movimentos = metodo(lista)
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"{nome} - Lista com {len(lista)}:")
    print(f"  - Comparações: {comparacoes}")
    print(f"  - Movimentos: {movimentos}")
    print(f"  - Tempo de execução: {tempo_execucao:.6f} segundos\n")
    return tempo_execucao


def ler_numeros_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        numeros = [int(line.strip()) for line in file]
    return numeros


def gerar_listas(nome_arquivo, tamanho):
    lista_random = ler_numeros_arquivo(nome_arquivo)
    lista_sorted = sorted(lista_random)
    lista_reversed = sorted(lista_random, reverse=True)
    return lista_random[:tamanho], lista_sorted[:tamanho], lista_reversed[:tamanho], "Aleatória", "Ordenada", "Reversa"


nome_arquivos = ['Artigo/numeros_5000.txt',
                 'Artigo/numeros_9000.txt', 'Artigo/numeros_12000.txt']
tamanhos = [5000, 9000, 12000]

tempos_bubble = []
tempos_selection = []
tempos_insertion = []

for nome_arquivo, tamanho in zip(nome_arquivos, tamanhos):
    numeros_random, numeros_sorted, numeros_reversed, nome_random, nome_sorted, nome_reversed = gerar_listas(
        nome_arquivo, tamanho)

    tempo_bubble_random = calcular_tempo_e_contagem(
        bubble_sort, numeros_random.copy(), f"Bubble Sort ({nome_random})")
    tempo_bubble_sorted = calcular_tempo_e_contagem(
        bubble_sort, numeros_sorted.copy(), f"Bubble Sort ({nome_sorted})")
    tempo_bubble_reversed = calcular_tempo_e_contagem(
        bubble_sort, numeros_reversed.copy(), f"Bubble Sort ({nome_reversed})")

    tempo_selection_random = calcular_tempo_e_contagem(
        selection_sort, numeros_random.copy(), f"Selection Sort ({nome_random})")
    tempo_selection_sorted = calcular_tempo_e_contagem(
        selection_sort, numeros_sorted.copy(), f"Selection Sort ({nome_sorted})")
    tempo_selection_reversed = calcular_tempo_e_contagem(
        selection_sort, numeros_reversed.copy(), f"Selection Sort ({nome_reversed})")

    tempo_insertion_random = calcular_tempo_e_contagem(
        insertion_sort, numeros_random.copy(), f"Insertion Sort ({nome_random})")
    tempo_insertion_sorted = calcular_tempo_e_contagem(
        insertion_sort, numeros_sorted.copy(), f"Insertion Sort ({nome_sorted})")
    tempo_insertion_reversed = calcular_tempo_e_contagem(
        insertion_sort, numeros_reversed.copy(), f"Insertion Sort ({nome_reversed})")

    tempos_bubble.append(
        [tempo_bubble_random, tempo_bubble_sorted, tempo_bubble_reversed])
    tempos_selection.append(
        [tempo_selection_random, tempo_selection_sorted, tempo_selection_reversed])
    tempos_insertion.append(
        [tempo_insertion_random, tempo_insertion_sorted, tempo_insertion_reversed])

plt.figure(figsize=(10, 8))

# Plotar curvas para Bubble Sort
for i, tamanho in enumerate(tamanhos):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_bubble],
             marker='o', label=f'Bubble Sort ({["Aleatória", "Ordenada", "Reversa"][i]})', linestyle='-')

# Plotar curvas para Selection Sort
for i, tamanho in enumerate(tamanhos):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_selection],
             marker='o', label=f'Selection Sort ({["Aleatória", "Ordenada", "Reversa"][i]})', linestyle='-')

# Plotar curvas para Insertion Sort
for i, tamanho in enumerate(tamanhos):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_insertion],
             marker='o', label=f'Insertion Sort ({["Aleatória", "Ordenada", "Reversa"][i]})', linestyle='-')

plt.title('Comparação de Tempos de Execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (segundos)')
plt.legend(title='Algoritmo', loc='upper left')
plt.grid(True)
plt.show()