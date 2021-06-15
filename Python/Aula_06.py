#01 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# sexo = 'M' or 'N'
# n = ''

# while n != sexo:
#     n = str(input('Digite seu Sexo: [M/F] ')).strip().upper()
#     if n == 'M':
#         print('Sexo Masculino')
#     elif n == 'N':
#         print('Sexo Feminino')
#     else:
#         print('Sexo Inválido')

# Desafio: Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# entre os palpites diga ao jogador se o número do computador é maior ou menor ao que ele digitou,
# no final mostre quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
usuario = int(input('Estou pensando em um número, tente adivinhar de 0 a 10: '))
palpite = 0

while usuario != computador:
    if usuario < computador:
        palpite += 1
        print('Não, pense em um número maior')
    elif usuario > computador:
        palpite += 1
        print('Não, pense em um número menor')
    else:
        break