#Desvio de Rota

import sys

INF = 100000
MAXSIZE = 101010

vis = [0] * MAXSIZE
dist = [INF] * MAXSIZE

class Node:
    def __init__(self, u, w):
        self.u = u
        self.w = w
        self.next = None

class Graph:
    def __init__(self, size):
        self.adj = [Node(None, None) for _ in range(size)]

def dijkstra(g, s, size):
    for i in range(size):
        dist[i] = INF
    vis = [False] * size
    dist[s] = 0

    for _ in range(size):
        v = -1
        for j in range(size):
            if not vis[j] and (v == -1 or dist[j] < dist[v]):
                v = j
        if dist[v] == INF:
            break
        vis[v] = True
        k = g.adj[v].next
        while k:
            to = k.u
            length = k.w
            if dist[v] + length < dist[to]:
                dist[to] = dist[v] + length
            k = k.next

def make_graph(size):
    g = Graph(size)
    return g

def make_node(u, w):
    return Node(u, w)

def push_back(g, u, v, w):
    new_node = make_node(u, w)
    new_node.next = g.adj[v].next
    g.adj[v].next = new_node

def main():
    for line in sys.stdin:
        n, m, c, k = map(int, line.split())
        if c == 0 and n == 0 and m == 0 and k == 0:
            break
        graph = make_graph(n + 1)
        for _ in range(m):
            a, b, w = map(int, sys.stdin.readline().split())
            if (a >= c and b >= c) or ((a < c) and (b < c) and (abs(a - b) == 1)):
                push_back(graph, a, b, w)
                push_back(graph, b, a, w)
            if a >= c and b < c:
                push_back(graph, b, a, w)
            if b >= c and a < c:
                push_back(graph, a, b, w)
        dijkstra(graph, k, n)
        print(dist[c - 1])

if __name__ == "__main__":
    main()
