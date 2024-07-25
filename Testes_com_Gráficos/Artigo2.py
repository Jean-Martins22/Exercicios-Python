import time
import random
import matplotlib.pyplot as plt

# Quick Sort


def quick_sort(lista):
    def _quick_sort(lista):
        nonlocal comparacoes, movimentos
        if len(lista) <= 1:
            return lista
        else:
            pivot = random.choice(lista)
            menores = [x for x in lista if x < pivot]
            iguais = [x for x in lista if x == pivot]
            maiores = [x for x in lista if x > pivot]

            comparacoes += len(lista) - 1
            movimentos += len(lista)

            return _quick_sort(menores) + iguais + _quick_sort(maiores)

    comparacoes = 0
    movimentos = 0
    sorted_list = _quick_sort(lista)
    return sorted_list, comparacoes, movimentos

# Merge Sort


def merge_sort(lista):
    def _merge_sort(lista):
        nonlocal comparacoes, movimentos
        if len(lista) > 1:
            meio = len(lista) // 2
            esquerda = lista[:meio]
            direita = lista[meio:]

            esquerda = _merge_sort(esquerda)
            direita = _merge_sort(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                comparacoes += 1
                if esquerda[i] < direita[j]:
                    lista[k] = esquerda[i]
                    i += 1
                else:
                    lista[k] = direita[j]
                    j += 1
                movimentos += 1
                k += 1

            while i < len(esquerda):
                lista[k] = esquerda[i]
                i += 1
                k += 1
                movimentos += 1

            while j < len(direita):
                lista[k] = direita[j]
                j += 1
                k += 1
                movimentos += 1

        return lista

    comparacoes = 0
    movimentos = 0
    sorted_list = _merge_sort(lista)
    return sorted_list, comparacoes, movimentos

# Heap Sort


def heapify(lista, n, i, comparacoes_movimentos):
    comparacoes, movimentos = comparacoes_movimentos
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n:
        comparacoes += 1
        if lista[i] < lista[esquerda]:
            maior = esquerda

    if direita < n:
        comparacoes += 1
        if lista[maior] < lista[direita]:
            maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        movimentos += 1
        comparacoes_movimentos[0] = comparacoes
        comparacoes_movimentos[1] = movimentos
        heapify(lista, n, maior, comparacoes_movimentos)


def heap_sort(lista):
    comparacoes = 0
    movimentos = 0
    n = len(lista)

    comparacoes_movimentos = [comparacoes, movimentos]

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, comparacoes_movimentos)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        comparacoes_movimentos[1] += 1
        heapify(lista, i, 0, comparacoes_movimentos)

    comparacoes, movimentos = comparacoes_movimentos
    return lista, comparacoes, movimentos

# Shell Sort


def shell_sort(lista):
    comparacoes = 0
    movimentos = 0
    n = len(lista)
    lacuna = n // 2

    while lacuna > 0:
        for i in range(lacuna, n):
            temp = lista[i]
            j = i
            while j >= lacuna:
                comparacoes += 1
                if lista[j - lacuna] > temp:
                    lista[j] = lista[j - lacuna]
                    movimentos += 1
                    j -= lacuna
                else:
                    break
            lista[j] = temp
            movimentos += 1
        lacuna //= 2

    return lista, comparacoes, movimentos


def calcular_tempo_e_contagem(metodo, lista, nome):
    inicio = time.time()
    lista_ordenada, comparacoes, movimentos = metodo(lista.copy())
    fim = time.time()
    tempo_execucao = fim - inicio
    print(f"{nome}:")
    print(f"  - Comparações: {comparacoes}")
    print(f"  - Movimentos: {movimentos}")
    print(f"  - Tempo de execução: {tempo_execucao:.6f} segundos\n")
    return tempo_execucao


def gerar_listas(nome_arquivo, tamanho):
    with open(nome_arquivo, 'r') as file:
        numeros = [int(line.strip()) for line in file]
    lista_random = numeros[:tamanho]
    lista_sorted = sorted(numeros[:tamanho])
    lista_reversed = sorted(numeros[:tamanho], reverse=True)
    return lista_random, lista_sorted, lista_reversed, "Aleatória", "Ordenada", "Reversa"


nome_arquivos = ['Artigo/numeros_100000.txt',
                 'Artigo/numeros_400000.txt', 'Artigo/numeros_700000.txt']
tamanhos = [100000, 400000, 700000]

tempos_quick = []
tempos_merge = []
tempos_heap = []
tempos_shell = []

for nome_arquivo, tamanho in zip(nome_arquivos, tamanhos):
    numeros_random, numeros_sorted, numeros_reversed, nome_random, nome_sorted, nome_reversed = gerar_listas(
        nome_arquivo, tamanho)

    tempo_quick_random = calcular_tempo_e_contagem(
        quick_sort, numeros_random.copy(), f"Quick Sort ({nome_random})")
    tempo_quick_sorted = calcular_tempo_e_contagem(
        quick_sort, numeros_sorted.copy(), f"Quick Sort ({nome_sorted})")
    tempo_quick_reversed = calcular_tempo_e_contagem(
        quick_sort, numeros_reversed.copy(), f"Quick Sort ({nome_reversed})")

    tempo_merge_random = calcular_tempo_e_contagem(
        merge_sort, numeros_random.copy(), f"Merge Sort ({nome_random})")
    tempo_merge_sorted = calcular_tempo_e_contagem(
        merge_sort, numeros_sorted.copy(), f"Merge Sort ({nome_sorted})")
    tempo_merge_reversed = calcular_tempo_e_contagem(
        merge_sort, numeros_reversed.copy(), f"Merge Sort ({nome_reversed})")

    tempo_heap_random = calcular_tempo_e_contagem(
        heap_sort, numeros_random.copy(), f"Heap Sort ({nome_random})")
    tempo_heap_sorted = calcular_tempo_e_contagem(
        heap_sort, numeros_sorted.copy(), f"Heap Sort ({nome_sorted})")
    tempo_heap_reversed = calcular_tempo_e_contagem(
        heap_sort, numeros_reversed.copy(), f"Heap Sort ({nome_reversed})")

    tempo_shell_random = calcular_tempo_e_contagem(
        shell_sort, numeros_random.copy(), f"Shell Sort ({nome_random})")
    tempo_shell_sorted = calcular_tempo_e_contagem(
        shell_sort, numeros_sorted.copy(), f"Shell Sort ({nome_sorted})")
    tempo_shell_reversed = calcular_tempo_e_contagem(
        shell_sort, numeros_reversed.copy(), f"Shell Sort ({nome_reversed})")

    tempos_quick.append(
        [tempo_quick_random, tempo_quick_sorted, tempo_quick_reversed])
    tempos_merge.append(
        [tempo_merge_random, tempo_merge_sorted, tempo_merge_reversed])
    tempos_heap.append(
        [tempo_heap_random, tempo_heap_sorted, tempo_heap_reversed])
    tempos_shell.append(
        [tempo_shell_random, tempo_shell_sorted, tempo_shell_reversed])

plt.figure(figsize=(10, 8))

# Estilos para os diferentes métodos de ordenação
estilos = {
    'Quick Sort': {'marker': 'o', 'linestyles': ['-', '--', '-.']},
    'Merge Sort': {'marker': 's', 'linestyles': ['-', '--', '-.']},
    'Heap Sort': {'marker': '^', 'linestyles': ['-', '--', '-.']},
    'Shell Sort': {'marker': 'd', 'linestyles': ['-', '--', '-.']}
}

# Plotar curvas para Quick Sort
for i, tipo in enumerate(["Aleatória", "Ordenada", "Reversa"]):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_quick],
             marker=estilos['Quick Sort']['marker'],
             label=f'Quick Sort ({tipo})',
             linestyle=estilos['Quick Sort']['linestyles'][i])

# Plotar curvas para Merge Sort
for i, tipo in enumerate(["Aleatória", "Ordenada", "Reversa"]):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_merge],
             marker=estilos['Merge Sort']['marker'],
             label=f'Merge Sort ({tipo})',
             linestyle=estilos['Merge Sort']['linestyles'][i])

# Plotar curvas para Heap Sort
for i, tipo in enumerate(["Aleatória", "Ordenada", "Reversa"]):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_heap],
             marker=estilos['Heap Sort']['marker'],
             label=f'Heap Sort ({tipo})',
             linestyle=estilos['Heap Sort']['linestyles'][i])

# Plotar curvas para Shell Sort
for i, tipo in enumerate(["Aleatória", "Ordenada", "Reversa"]):
    plt.plot(tamanhos, [tempo[i] for tempo in tempos_shell],
             marker=estilos['Shell Sort']['marker'],
             label=f'Shell Sort ({tipo})',
             linestyle=estilos['Shell Sort']['linestyles'][i])

plt.title('Comparação de Tempos de Execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (segundos)')
plt.legend(title='Algoritmo', loc='upper left')
plt.grid(True)
plt.show()
