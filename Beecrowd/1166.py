#Torre de Hanoi, Novamente!

bolas = [(i + 1) * (i + 1) // 2 - 1 for i in range(100)]
t = int(input())
for _ in range(t):
  n = int(input())
  print(bolas[n])