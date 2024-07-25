#3. Faça, em Python, o cálculo do maior divisor comum e do menor múltiplo comum usando o Teorema Fundamental da Aritmética.

def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

def mdc(a, b):
    fatores_a = fatores_primos(a)
    fatores_b = fatores_primos(b)
    i = j = 0
    resultado = 1
    while i < len(fatores_a) and j < len(fatores_b):
        if fatores_a[i] == fatores_b[j]:
            resultado *= fatores_a[i]
            i += 1
            j += 1
        elif fatores_a[i] < fatores_b[j]:
            i += 1
        else:
            j += 1
    return resultado

def mmc(a, b):
    return (a * b) // mdc(a, b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado_mdc = mdc(num1, num2)
resultado_mmc = mmc(num1, num2)

print("O MDC de", num1, "e", num2, "é:", resultado_mdc)
print("O MMC de", num1, "e", num2, "é:", resultado_mmc)
