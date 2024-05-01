nomes = []
for i in range(0, 10):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

for j in range(0, 10):
    if j == 2 or j == 6 or j == 8:
        print(nomes[j])
