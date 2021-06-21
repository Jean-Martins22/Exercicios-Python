#01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

# from random import sample

# numero = tuple(sample(range(50), 5))
# for a in numero:
#     print(a, end = ' ')
# print(f'''
# Maior valor sorteado: {max(numero)}
# Menor valor sorteado: {min(numero)}.''')


#02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

# numero = (int(input('1º valor:')), int(input('2º valor:')), int(input('3º valor:')), int(input('4º valor:')))
# print(numero)
# print(f'O número 9 aparece {numero.count(9)} vezes.')
# if 3 in numero:
#     print(f'O número 3 foi digitado pela primeira vez na posição {numero.index(3)}')
# else:
#     print('O número 3 não foi digitado')

# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

# l = [5, 7, 2, 9, 4, 1, 3]
# soma = sum(l)
# print(f'O tamanho da lista é: {len(l)}')
# print(f'O maior valor da lista é: {max(l)}')
# print(f'O menor valor da lista é: {min(l)}')
# print(f'A Soma é: {soma}')
# l.sort()
# print(f'Crescente {l}')
# l.reverse()
# print(f'Decrescente {l}')

# Desafio da noite: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"  O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = list(["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","você ja trabalhou com a vítima? "])
resposta = ""
resultado =list(["Inocente","Suspeita","Cumplice","Cumplice","Assassino"])
culpa = 0
for i in range(5):
    resposta = input(perguntas[i]).strip().lower()
    if resposta.startswith("s"):
        culpa += 1
if culpa == 1:
    print(f"Você é um(a): {resultado[culpa]}")
else:
    print(f"Você é um(a): {resultado[culpa-1]}")