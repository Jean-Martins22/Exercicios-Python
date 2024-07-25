#Tribol

import sys

def main():
    adj = [[0, 2, 1], [1, 0, 2], [2, 1, 0], [0, 0, 0]]
    ans = ["red", "green", "blue", "empate", "trempate"]

    n = int(input())

    for _ in range(n):
        q = int(input())
        adj[3] = [0, 0, 0]

        for _ in range(q):
            a, b = input().split()
            if a == 'R':
                u = 0
            elif a == 'G':
                u = 1
            else:
                u = 2

            if b == 'R':
                v = 0
            elif b == 'G':
                v = 1
            else:
                v = 2

            adj[3][u] += adj[u][v]

        maior = adj[3][0]
        cont = 0

        for i in range(1, 3):
            if adj[3][i] > maior:
                maior = adj[3][i]
                cont = i
            elif adj[3][i] == maior:
                cont = 3

        if adj[3][0] == adj[3][1] == adj[3][2]:
            cont = 4

        print(ans[cont])

if __name__ == "__main__":
    main()
