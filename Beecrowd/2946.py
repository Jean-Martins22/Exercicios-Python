#Dabriel e a Divisibilidade

def divisivel_por_n(binario, numeros):
    n_decimal = int(binario, 2)
    divisores = []

    for numero in numeros:
        if n_decimal % numero == 0:
            divisores.append(numero)

    return sorted(divisores) if divisores else "Nenhum"

if __name__ == "__main__":
    binario = input().strip()
    m = int(input().strip())
    numeros = [int(input().strip()) for _ in range(m)]
    
    resultado = divisivel_por_n(binario, numeros)
    if resultado == "Nenhum":
        print(resultado)
    else:
        print(" ".join(map(str, resultado)))
