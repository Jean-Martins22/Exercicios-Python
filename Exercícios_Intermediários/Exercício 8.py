#Teorema Chines

def mod_inverso(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def teorema_chines_do_resto(congruencias):
    N = 1
    for _, modolos in congruencias:
        N *= modolos

    resultados = 0
    for residuo, modolos in congruencias:
        ni = N // modolos
        mi = mod_inverso(ni, modolos)
        resultados += residuo * ni * mi

    return resultados % N


congruencias = [(5, 7), (7, 11), (3, 13)]

x = teorema_chines_do_resto(congruencias)

print("O menor inteiro positivo x é:", x)
