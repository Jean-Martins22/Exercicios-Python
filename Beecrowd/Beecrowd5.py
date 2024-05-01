def refrigerantes(E, F, C):
    total = E + F
    bebidos = 0

    while total >= C:
        novo = total // C
        total = novo + total % C
        bebidos += novo

    return bebidos

E, F, C = map(int, input().split())

print(refrigerantes(E, F, C))
