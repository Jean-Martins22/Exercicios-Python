N = int(input("Quantos nomes tem na lista: "))
nomes = list(input("Digite os nomes: ").split())

bem = 0
mal = 0
nomes_ordenados = []

for i in range(0, N*2):
    if nomes[i] != "+" and nomes[i] != "-":
        nomes_ordenados.append(nomes[i])
    if nomes[i] == "+":
        bem += 1
    elif nomes[i] == "-":
        mal += 1

nomes_ordenados.sort()
for j in nomes_ordenados:
    print(j)

print(f"Se comportaram: {bem} | Nao se comportaram: {mal}")

'''
N = int(input())
criancas = []
bem_comportadas = 0
mal_comportadas = 0

for _ in range(N):
    comportamento, nome = input().split()
    criancas.append(nome)
    if comportamento == '+':
        bem_comportadas += 1
    else:
        mal_comportadas += 1

criancas.sort()

for nome in criancas:
    print(nome)

print("Se comportaram: {} | Nao se comportaram: {}".format(bem_comportadas, mal_comportadas))

'''