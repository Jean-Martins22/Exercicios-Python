# from time import sleep
# cont = 10

# while cont != 0:
#    print(cont)
#    sleep(1)
#    cont -= 1 # Diminui 1 do cont a cada volta do laço
# print('FELIZ ANO NOVOOO!')

# n = 1
# while n != 0: # O while é um laço com condição de parada, ENQUANTO o n for diferente de zero, faça...
#    n = int(input('Digite um valor: '))
# print('Fim')

n = 1 # isso é gambiarra, while com break
par = impar = 0
while n != 0:
   n = int(input('Digite um valor: '))
   if n != 0:
      if n % 2 == 0:
         par += 1
      else:
         impar += 1

print(f'Você digitou {par} numeros pares e {impar} números impares!')