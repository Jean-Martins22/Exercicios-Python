#Prefixa, Infixa e Posfixa

class Node:
    def __init__(self, letra):
        self.letra = letra
        self.esquerda = None
        self.direita = None

def novo_no(letra):
    return Node(letra)

def src(string, inicio, fim, letra):
    for i in range(inicio, fim + 1):
        if string[i] == letra:
            return i
    return -1

def tree(infixa, prefixa, inInicio, inFim):
    global indice
    if inInicio > inFim:
        return None

    no = novo_no(prefixa[indice])
    indice += 1

    if inInicio == inFim:
        return no

    infixaIndice = src(infixa, inInicio, inFim, no.letra)
    no.esquerda = tree(infixa, prefixa, inInicio, infixaIndice - 1)
    no.direita = tree(infixa, prefixa, infixaIndice + 1, inFim)

    return no

def show_posfixa(no):
    if no is None:
        return

    show_posfixa(no.esquerda)
    show_posfixa(no.direita)
    print(no.letra, end='')

if __name__ == "__main__":
    qtsCasos = int(input())

    for _ in range(qtsCasos):
        qtsNodes, prefixa, infixa = input().split()
        qtsNodes = int(qtsNodes)
        indice = 0
        raiz = tree(infixa, prefixa, 0, qtsNodes - 1)
        show_posfixa(raiz)
        print()
