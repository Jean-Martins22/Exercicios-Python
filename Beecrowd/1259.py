#Pares e Ímpares

lista = []
listaP = []
listaN = []

x = int(input())

for i in range(x):
    y = int(input())
    lista.append(y)
    

for i in lista:
    if i % 2 == 0:
        listaP.append(i)
    else:
        listaN.append(i)

listaP.sort()
listaN.sort(reverse=True)

for i in listaP:
    print(i)

for i in listaN:
    print(i)