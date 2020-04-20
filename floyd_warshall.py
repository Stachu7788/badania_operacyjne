import numpy as np
from copy import deepcopy
from graph import Graph
from simple_map import Map


def floyd_warshall(G: Graph, start = None, stop = None):
    n = len(G)
    d = G.M()
    prev = np.multiply(np.arange(n, dtype=int),
                       np.ones([n, n], dtype=int)).T.tolist()
    for u in range(n):
        for v1 in range(n):
            for v2 in range(n):
                if d[v1][v2] > d[v1][u] + d[u][v2]:
                    d[v1][v2] = round(d[v1][u]+d[u][v2], 2)
                    prev[v1][v2] = prev[u][v2]
    if start is None:
        return (d,prev)
    dct = Map(start,n)
    for i in range(n):
        dct[i] = [d[start][i], prev[start][i]]
    if stop is None:
        return dct
    else:
        return  dct.reconstruct_path(start,stop)
                
