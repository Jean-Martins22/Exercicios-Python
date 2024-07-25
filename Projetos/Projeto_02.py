# Projeto Pedra, Papel e Tesoura

from random import randint # Da biblioteca random importar randint.
from time import sleep # Da biblioteca time importar sleep.
itens = ('Pedra', 'Papel', 'Tesoura') # Lista com as escolhas.

while True:
    vitorias = 0 # Contador de vitórias do jogador.
    vitorias_computador = 0 # Contador de vitórias do Computador.
    for i in range(int(input('Digite quantos jogos vai querer jogar: '))): # Pede para o jogador digitar quantas vezes ele quer jogar.
        print('''Suas opções:
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura
        ''')

        jogador = int(input('Qual será a sua jogada ? ')) # Pergunta ao jogador o que ele irá escolher.
        computador = randint(0, 2) # Faz o computador escolher entra Pedra, Papel e Tesoura.
        
        print('JO') # Deixa bonito.
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        print('-=-' * 10)
        print('O computador jogou {}'.format(itens[computador])) # Mostra a escolha do computador.
        print('O jogador jogou {}'.format(itens[jogador])) # Mostra a escolha do jogador.
        print('-=-' * 10) # Deixa bonito.

        if computador == 0: # Computador jogou Pedra...
            if jogador == 0: # Se o jogador também jogar Pedra...
                print('Empate') # Da empate.
            elif jogador == 1:
                vitorias += 1
                print('Jogador Venceu')
            elif jogador == 2:
                print('Jogadaor Perdeu')
                vitorias_computador += 1
            else:
                print('Jogada Inválida!')
        elif computador == 1: # Computador jogou Papel.
            if jogador == 0:
                vitorias_computador += 1
                print('Jogador Perdeu')
            elif jogador == 1:
                print('Empate')
            elif jogador == 2:
                vitorias += 1
                print('Jogador Venceu')
            else:
                print('Jogada Inválida!')
        elif computador == 2: # Computador jogou Tesoura.
            if jogador == 0:
                vitorias += 1
                print('Jogador Venceu')
            elif jogador == 1:
                vitorias_computador += 1
                print('Jogador Perdeu')
            elif jogador == 2:
                print('Empate')
            else:
                print('Jogada Inválida!')

    if vitorias > vitorias_computador: # Se as vitórias do Jogador forem maiores que as do Computador, o Jogador vence.
        print('-=-' * 18)
        print(f'O jogador ganhou {vitorias} vezes, o computador ganhou {vitorias_computador} vezes.\n O Campeão foi o Jogador 😁')
        print('-=-' * 18)
    elif vitorias_computador > vitorias: # Se as vitórias do Computador forem maiores que as do Jogador, o Computador vence.
        print('-=-' * 18)
        print(f'O jogador ganhou {vitorias} vezes, o computador ganhou {vitorias_computador} vezes.\n O Campeão foi o Computador 🤖')
        print('-=-' * 18)
    else:
        print('-=-' * 18)
        print(f'O jogador ganhou {vitorias} vezes, o computador ganhou {vitorias_computador} vezes.\n Parece que deu Empate 🧐')
        print('-=-' * 18)
    tentar_denovo = str(input('Quer jogar novamente ? [S/N] ')).strip().lower()[0] # Pergunta se o jogador quer jogar denovo
    if tentar_denovo == 'n': # Se a resposta for não...
        break # Acaba com o While