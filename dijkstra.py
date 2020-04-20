import numpy as np
from graph import Graph
from simple_map import Map


def dijkstra(G: Graph, start: int, stop: int = None):
    dct = Map(start, len(G))
    not_visited = np.arange(0, len(G), 1).tolist()
    u = start
    while u is not None:
        not_visited.remove(u)
        for v in G.get_neighbours(u):
            if dct[v][0] > dct[u][0] + G[u][v]:
                dct[v] = [round(dct[u][0]+G[u][v], 2), u]
        u = dct.get_closest_from(not_visited)
    if stop is None:
        return dct
    else:
        return dct.reconstruct_path(start, stop)
