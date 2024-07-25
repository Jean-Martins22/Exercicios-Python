#Consecutivos

N = int(input())
valores = list(map(int, input().split()))

max_seq = 0
atual_seq = 1

for i in range(1, N):
    if valores[i] == valores[i - 1]:
        atual_seq += 1
    else:
        atual_seq = 1
    if atual_seq > max_seq:
        max_seq = atual_seq
print(max_seq)
