'''
1. Faça um código em Python que use a estrutura de dados pilha para verificar o balanceamento dos 
parênteses, colchetes e chaves em expressões aritméticas:
'''

def verifica_expressao_simples(expressao):
    pilha = []
    for char in expressao:
        if char in "([{":
            pilha.append(char)
        elif char in ")]}":
            if not pilha:
                return False
            if char == ")" and pilha[-1] != "(" or \
               char == "]" and pilha[-1] != "[" or \
               char == "}" and pilha[-1] != "{":
                return False
            pilha.pop()
    return not pilha

def verifica_expressao_composta(expressao):
    return verifica_expressao_simples(expressao)

print('Expressoes simples\n')
print(verifica_expressao_simples('((1 + 2) * (3 + 4)) - (5 + 6)'))
print()
print(verifica_expressao_simples('((1 + 2) * (3 + 4))))'))
print()
print(verifica_expressao_simples('(((((1 + 2) * (3 + 4))'))
print()
print('Expressoes compostas\n')
print(verifica_expressao_composta('{ [ (1 + 2) + (3 + 4) ] * 2 }'))
print()
print(verifica_expressao_composta('{ [ (1 + 2} + [3 + 4} ) * 2 )'))