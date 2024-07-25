import networkx as nx  # Usada para criar e manipular grafos
import matplotlib.pyplot as plt  # Usada para desenhar grafos
from itertools import combinations  # Usada para gerar combinações de nós


def draw_graph(G, path=None):
    # Define a posição dos nós no gráfico
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 8))

    # Desenha os nós e arestas do grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            edge_color='gray', node_size=700, font_size=15)

    if path:
        # Se um caminho euleriano for fornecido, desenha as arestas no caminho
        edge_list = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        edge_list.append((path[-1], path[0]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_list,
                               edge_color='r', width=2)

    plt.show()


def make_eulerian(G):
    # Encontra nós com grau ímpar
    odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]

    # Enquanto houver nós com grau ímpar, emparelha e adiciona arestas
    while len(odd_degree_nodes) > 0:
        for u, v in combinations(odd_degree_nodes, 2):
            if not G.has_edge(u, v):
                G.add_edge(u, v)
                # Atualiza a lista de nós com grau ímpar após adicionar uma aresta
                odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]
                break
        else:
            break

    return G


def is_eulerian(G):
    # Verifica se o grafo é euleriano usando função da NetworkX
    return nx.is_eulerian(G)


def find_eulerian_circuit(G):
    # Encontra e retorna o circuito euleriano
    return list(nx.eulerian_circuit(G))


def main():
    # Exemplo de um grafo não euleriano mas que vira um
    edges_eulerian = [(0, 1), (1, 2), (2, 3), (3, 0),
                      (0, 2), (2, 4), (4, 1), (4, 3)]

    # Cria o grafo e adiciona as arestas
    G = nx.Graph()
    G.add_edges_from(edges_eulerian)

    print("Grafo inicial:")
    draw_graph(G)

    if not is_eulerian(G):
        print("O grafo não é Euleriano. Transformando em Euleriano...")
        G = make_eulerian(G)
        print("Grafo transformado:")
        draw_graph(G)

    if is_eulerian(G):
        print("O grafo é Euleriano. Encontrando o circuito Euleriano...")
        eulerian_path = find_eulerian_circuit(G)
        eulerian_path_nodes = [edge[0]
                               for edge in eulerian_path] + [eulerian_path[-1][1]]
        print("Caminho Euleriano:", eulerian_path_nodes)
        draw_graph(G, eulerian_path_nodes)
    else:
        print("Não foi possível transformar o grafo em Euleriano.")


if __name__ == "__main__":
    main()
