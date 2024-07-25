'''
2. Implemente uma função em Python que 
converta um número inteiro arbitrário na base 
10 (decimal) para a representação binária.
'''

def converte_para_binario():
    n = int(input("Digite um número inteiro: "))
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario

print(converte_para_binario())