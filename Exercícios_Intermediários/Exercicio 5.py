#• 1. Faça, em Python, o cálculo do maior divisor comum entre dois números.

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    while num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    print("O maior divisor comum entre os números é:", num1)
    
except ValueError:
    print("Por favor, insira apenas números inteiros.")