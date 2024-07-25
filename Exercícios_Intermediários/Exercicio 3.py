'''
3. Implemente sua agenda de contatos e busque o telefone de um amigo.
'''

import random


def gera_telefone():
    return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"


agenda = {
    "Jean": gera_telefone(),
    "Bruno": gera_telefone(),
    "Silvia": gera_telefone(),
    "Eduardo": gera_telefone(),
    "Kanye": gera_telefone(),
}

nome = input("Digite o nome do amigo: ")
telefone = agenda.get(nome)

if telefone:
    print(f"O telefone de {nome} é {telefone}.")
else:
    print(f"Não foi encontrado um contato com o nome {nome}.")
