#DFSr - Hierarquia de Profundidade

MAXSIZE = 30
def dfs(u):
    global flag
    global esp
    vis[u] = True
    esp += "  "

    for i in range(v):
        if adj[u][i]:
            flag = True
            if not vis[i]:
                print("{}{}-{} pathR(G,{})".format(esp, u, i, i))
                dfs(i)
                esp = esp[:-2]
            else:
                print("{}{}-{}".format(esp, u, i))

caso = 0
n = int(input())

while n > 0:
    n -= 1
    v, e = map(int, input().split())
    vis = [False] * MAXSIZE
    adj = [[False] * MAXSIZE for _ in range(MAXSIZE)]

    for _ in range(e):
        u, w = map(int, input().split())
        adj[u][w] = True

    print("Caso {}:".format(caso + 1))
    caso += 1
    for i in range(v):
        esp = ""
        flag = False
        if not vis[i]:
            dfs(i)

        if flag:
            print()
