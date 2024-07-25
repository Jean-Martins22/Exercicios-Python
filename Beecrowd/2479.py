#Ordenando a Lista de Crianças do Papai Noel

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
