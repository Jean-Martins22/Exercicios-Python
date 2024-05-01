from collections import deque

def jogar_cartas():
    # Recebe a entrada do usuário
    n = int(input("Digite o número de cartas: "))

    # Cria a fila de cartas
    cartas = deque(range(1, n+1))

    # Lista para armazenar a sequência de cartas descartadas
    descartadas = []

    while len(cartas) > 1:
        # Descarta a carta do topo
        descartadas.append(str(cartas.popleft()))

        # Move a próxima carta para a base da fila
        cartas.rotate(-1)

    # Formata a saída
    descartadas_str = ', '.join(descartadas)
    print("Discarded cards: " + descartadas_str)
    print("Remaining card: " + str(cartas[0]))

# Chama a função
jogar_cartas()
