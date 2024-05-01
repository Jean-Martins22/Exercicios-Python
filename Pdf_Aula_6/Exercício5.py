# Crivo de Erastotenes

def crivo_de_erastotenes(n):
    primes = [True] * (n+1)

    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(n+1) if primes[i]]


n = int(input("Digite um número inteiro n >= 0: "))
if n < 0:
    print("O número precisa ser maior ou igual a zero.")
else:
    primes = crivo_de_erastotenes(n)
    print("Números primos até", n, ":", primes)
