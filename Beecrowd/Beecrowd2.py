'''
Num sorteio que distribui prêmios, um participante inicialmente sorteia um inteiro N e depois N valores. 
O número de pontos do participante é o tamanho da maior sequência de valores consecutivos iguais. 
Por exemplo, suponhamos que um participante sorteia N = 11 e, nesta ordem, os valores

30, 30, 30, 30, 40, 40, 40, 40, 40, 30, 30

Então, o participante ganha 5 pontos, correspondentes aos 5 valores 40 consecutivos. 
Note que o participante sorteou 6 valores iguais a 30, mas nem todos são consecutivos.

Sua tarefa é ajudar a organização do evento, escrevendo um programa que determina o número de pontos de um participante.
'''

N = int(input("Digite o número de valores a serem sorteados: "))
valores = list(map(int, input("Digite os valores: ").split()))

max_seq = 0
atual_seq = 1

for i in range(1, N):
    if valores[i] == valores[i - 1]:
        atual_seq += 1
    else:
        atual_seq = 1
    if atual_seq > max_seq:
        max_seq = atual_seq
print(max_seq)
