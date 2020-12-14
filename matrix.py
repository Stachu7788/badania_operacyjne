import numpy as np
from prima import prima
from graph import Graph
"""
nodes - liczba wierzchołków
height x width - rozmiar siatki
dst - maksymalna odległość między wierzchołkami by te się połączyły
edges - liczba krawędzi (bierze piorytet nad dst)
"""


def create_matrix(height: int, width: int, nodes: int = 10, **dct):
    edges: int = dct.pop('edges', None)
    dst: int = dct.pop('dst', 5)
    while True:
        x = np.random.randint(0, width, size=nodes)
        y = np.random.randint(0, height, size=nodes)
        temp = set()
        for i in range(nodes):
            temp.add((x[i], y[i]))
        if len(temp) == len(x):
            break
    T = np.zeros([nodes, nodes])
    M = np.ones([nodes, nodes])*np.inf
    con = {}
    for i in range(nodes):
        T[i][i] = 0
        M[i][i] = 0
        for j in range(i+1, nodes):
            T[i][j] = T[j][i] = round(np.sqrt((x[i]-x[j])**2 +
                                      (y[i]-y[j])**2), 2)
            con[i, j] = T[i][j]
    if edges:
        items = list(con.items())
        sort = sorted(items, key=lambda tup: tup[1])
        for i in range(edges):
            u, v = sort[i][0]
            dst = sort[i][1]
            M[u][v] = M[v][u] = dst
    else:
        M = np.where(T[:][:] <= dst, T[:][:], np.inf)
    return M, T, x, y, con


def get_coherent_graph():
    while True:
        G = Graph(*create_matrix(20, 20, 10))
        p = prima(G, 0)
        c = p[0]
        if len(c) == 9:
            return G


def graph_for_taboo(nodes: int):
    while True:
        G = Graph(*create_matrix(20, 20, nodes))
        p = prima(G, 0)
        c = p[0]
        if len(c) == nodes - 1:
            return G
