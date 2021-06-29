# Importanto a biblioteca randint para escolher aleatóriamente

from random import randint

# Importanto a biblioteca sleep para fazer pausas durante um print e outro

from time import sleep

# Mostrando a apresentação do campeonato e as Regras

print('-=-' * 32)
print('                   Sejam bem vindos ao campeonato de dados 🎲 RocketZada               ')
sleep(1)
print('Queijão 🧀: Sou o apresentador Queijão e hoje iremos ter uma disputa de dados entre os jogadores: ')
print('-=-' * 32)
print()
print('=' * 10, 'Jogadores', '=' * 10)
sleep(1)
print('Jean 😃')
sleep(1)
print('Antonio 😄')
sleep(1)
print('Jonas 😁')
sleep(1)
print('Ricardo 😆')
print('=' * 31)
print()
print('-=-' * 12)
print('Queijão 🧀: Vamos explicar as regras')
print('-=-' * 12)
print()
print('=' * 37, 'Regras', '=' * 37)
print('A cada rodada os jogadores deverão rodar o dado 1 vez')
sleep(1)
print('Quem tirar o maior número será o vencedor')
sleep(1)
print('Caso der empate durante uma rodada o jogo será desconsiderado')
sleep(1)
print('Em RocketZada poderá haver mais de um campeão')
sleep(1)
print('E se jogarem mais de 1 rodada, as vitórias serão somadas e mostradas no final.')
print('=' * 82)
print()
print('-=-' * 36)
print('Queijão 🧀: Que tal você nosso caro espectador escolher quantas rodadas nossos queridos jogadores irão fazer ?')
print('-=-' * 36)
print()

dicionario = dict() # Dicionário crido para guardar os valores de cada rodada
jean = antonio = jonas = ricardo = empate = 0 # Variáveis criadas para guardas as vitórias de cada jogador

for i in range(int(input('Digite quantos jogos iremos fazer hoje: '))): # Pergunta ao usuário quantos jogos vai querer fazer
    dicionario['Jean'] = randint(1, 6) # Escolhe um número aleatório para os jogadores (Linha 53 até 56)
    dicionario['Antonio'] = randint(1, 6)
    dicionario['Jonas'] = randint(1, 6)
    dicionario['Ricardo'] = randint(1, 6)
    print() # Formatação
    print('Rodando os dados... 🕗')
    print()
    sleep(3)
    print('=' * 10, 'Resultados desta Rodada', '=' * 10) # Mostra os resultados de cada partida (Linha 61 até 69)
    print(f"Jean 😃: {dicionario['Jean']}")
    sleep(1)
    print(f"Antonio 😄: {dicionario['Antonio']}")
    sleep(1)
    print(f"Jonas 😁: {dicionario['Jonas']}")
    sleep(1)
    print(f"Ricardo 😆: {dicionario['Ricardo']}")
    print('=' * 45)

# Calcula os possíveis resultados dos jogos (Linha 73 até 104)

    if dicionario['Jean'] > dicionario['Antonio'] and dicionario['Jean'] > dicionario['Jonas'] and dicionario['Jean'] > dicionario['Ricardo']:
        jean += 1 # Adiciona mais 1 as vitórias do jogador
        print('O vencedor desta rodada foi...') # Formatação
        sleep(2)
        print('Jean 😃')
    
    elif dicionario['Antonio'] > dicionario['Jean'] and dicionario['Antonio'] > dicionario['Jonas'] and dicionario['Antonio'] > dicionario['Ricardo']:
        antonio += 1
        print('O vencedor desta rodada foi...')
        sleep(2)
        print('Antonio 😄')
    
    elif dicionario['Jonas'] > dicionario['Jean'] and dicionario['Jonas'] > dicionario['Antonio'] and dicionario['Jonas'] > dicionario['Ricardo']:
        jonas += 1
        print('O vencedor desta rodada foi...')
        sleep(2)
        print('Jonas 😁')
    
    elif dicionario['Ricardo'] > dicionario['Jean'] and dicionario['Ricardo'] > dicionario['Antonio'] and dicionario['Ricardo'] > dicionario['Jonas']:
        ricardo += 1
        print('O vencedor desta rodada foi...')
        sleep(2)
        print('Ricardo 😆')
    
    else:
        print()
        ('-=-' * 14)
        sleep(1)
        print('Queijão 🧀: Parece que deu empate ⛔, essa rodada será desconsiderada!. Pois só pode haver 1 vencedor por rodada')
        sleep(1)
        ('-=-' * 14)
        empate += 1

# Mostra os resultados finais

print()
print('-=-' * 12)
print('Queijão 🧀: Os resultados finais são:')
print('-=-' * 12)
print()
print('=' * 10, 'Resultados', '=' * 10)
print(f'Jean 😃 ganhou: {jean} vezes')
sleep(1)
print(f'Atonio 😄 ganhou: {antonio} vezes')
sleep(1)
print(f'Jonas 😁 ganhou: {jonas} vezes')
sleep(1)
print(f'Ricardo 😆 ganhou: {ricardo} vezes')
sleep(1)
print(f'Foram desconsiderados: {empate} empates ⛔')
print('=' * 32)
