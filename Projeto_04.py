from datetime import datetime
from time import sleep
import os

votos = list()
contadorvotos = list([0,0,0,0,0])

opcoes = """- 1 - Queijão 🧀.- 2 - Xoninhas 🍗.- 3 - Biferti 🥩.- 4 - Voto Nulo ⚫.- 5 - Voto em Branco ⚪"""

def autoriza_voto(anodenascimento):
    date = datetime.now()
    anos = date.year - anodenascimento
    if anos > 16 and anos < 18 and anos > 70:
        return 'OPCIONAL'
    elif anos < 16:
        return 'NEGADO'
    else:
        return 'OBRIGATÓRIO'
def votacao(autorizacao,valorvoto):
    voto = dict()
    if autorizacao == 'NEGADO':
        return 'Você não pode votar!'
    else:
        contadorvotos[valorvoto-1]+=1
        votos.append(voto)
        return 'Voto realizado com sucesso!'
def mostra_candidatos():
    tabela = " ".center(52).replace(" ","_")+"\n"
    tabela+= "|"+"candidatos e opções".center(50)+"|\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|\n"
    opcao = opcoes.split(".")
    for i in range(5):
       tabela+=f"|{opcao[i].ljust(50)}|\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|\n"
    return tabela
def imprime_resultado():
    tabela = " ".center(58).replace(" ","_")+"\n"
    tabela += "|"+"candidatos e opções".center(50)+"|votos|\n"
    tabela += "| ".ljust(51).replace(" ","_")+"|_____|\n"
    opcao = opcoes.split(".")
    for i in range(5):
       tabela+=f"|{opcao[i].ljust(50)}|{str(contadorvotos[i]).center(5)}|"+"\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|_____|\n"
    tabela+=f"\n O vencedor nesta votação é:{opcao[(contadorvotos.index(max(contadorvotos)))]}"
    return tabela
def espera(numeroespera):
    os.system('cls' if os.name == 'nt' else 'clear')
    esperar = ""
    for i in range(numeroespera):    
        esperar += "● "
        print(esperar)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
existeoutroeleitor="s"
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if existeoutroeleitor.startswith("s"):
        nascimentoeleitor = int(input("digite o ano de nascimento do eleitor: "))
        autoriza = autoriza_voto(nascimentoeleitor)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seu status para votação é de:",autoriza)
        sleep(2)
        espera(3)
        print(mostra_candidatos())
        valorvoto = int(input("digite sua escolha: "))
        espera(3)
        print(votacao(autoriza,valorvoto))
        sleep(3)
        espera(3)
        existeoutroeleitor = input("Existe um próximo eleitor? ").strip(" ").lower()
        
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contabilizando votos .")
        sleep(1)
        espera(10)
        print(imprime_resultado())
        break