from graph import Graph
from simple_map import Map


def bellman_ford(G: Graph, start: int, stop: int = None):
    n = len(G)
    tab = Map(start, n)
    for _ in range(n-1):
        for u, v in G.get_connections():
            if tab[v][0] > tab[u][0] + G[u][v]:
                tab[v][0] = round(tab[u][0]+G[u][v], 2)
                tab[v][1] = u
    if stop is not None:
        return tab.reconstruct_path(start, stop)
    else:
        return tab
