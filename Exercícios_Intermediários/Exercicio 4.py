# 4. Faça, em Python, o cálculo do fatorial usando os fatores primos.

def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

def fatorial_com_fatores_primos(num):
    fatores_fatorial = []
    for i in range(2, num + 1):
        fatores_i = fatores_primos(i)
        fatores_fatorial.extend(fatores_i)

    resultado = 1
    for fator in fatores_fatorial:
        resultado *= fator

    return resultado

num = int(input("Digite um número para calcular o fatorial: "))

resultado_fatorial = fatorial_com_fatores_primos(num)
print("O fatorial de", num, "é:", resultado_fatorial)
