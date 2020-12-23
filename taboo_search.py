from graph import Graph
import numpy as np
from typing import List


def taboo_search(G: Graph, profit: np.ndarray, s0: List[int],
                 loss_coeficient: float):
    graph_data = G, profit, loss_coeficient
    sBest = s0
    bestCandidate = s0
    fitness_lst = [fitness(*graph_data, s0)]
    tabuList = []
    neig_num = []
    candidates = []
    tabuList.append(s0)
    iterations_wo_change = 0
# =============================================================================
#     while iterations_wo_change < 200:
# =============================================================================
    for i in range(60):
        iterations_wo_change += 1
        sNeighbourhood = get_neighbours(G, bestCandidate)
        neig_num.append(len(sNeighbourhood))
        bestCandidate = sNeighbourhood[0]
        for sCandidate in sNeighbourhood:
            if(sCandidate not in tabuList and
               fitness(*graph_data, sCandidate) > fitness(*graph_data,
                                                          bestCandidate)):
                bestCandidate = sCandidate
        fitness_lst.append(fitness(*graph_data, bestCandidate))
        candidates.append(bestCandidate)
        if fitness(*graph_data, bestCandidate) > fitness(*graph_data, sBest):
            sBest = bestCandidate
            iterations_wo_change = 0
        tabuList.append(bestCandidate)
    return sBest, fitness_lst, neig_num, candidates


def get_neighbours(G: Graph, sol: List[int]):
    paths = G.shortest_paths()
    vertices = G.get_neighbours()
    neigbours = []
    neigbours.append(sol[1:])
    neigbours.append(sol[:-1])
    for num in [1, 2, 3]:
        diff = num + 1
        for i in range(len(sol)-diff):
            u, v = sol[i], sol[i+diff]
            if u == v:
                continue
            insert = paths[u][v][1:-1]
            if not len(insert):
                common = set(vertices[u]) & set(vertices[v])
                if common:
                    for vertex in common:
                        neigbours.append(sol[:i]+[vertex]+sol[i+diff:])
            neigbours.append(sol[:i]+insert[:]+sol[i+diff:])
    for i in range(len(sol) - 1):
        u, v = sol[i], sol[i+1]
        common = set(vertices[u]) & set(vertices[v])
        if common:
            for vertex in common:
                neigbours.append(sol[:i]+[vertex]+sol[i+1:])
        for u_neig in vertices[u]:
            common = set(vertices[u_neig]) & set(vertices[v])
            if common:
                try:
                    common.remove(u)
                except KeyError:
                    pass
                for vertex in common:
                    neigbours.append(sol[:i]+[u_neig, vertex]+sol[i+1:])
    return neigbours

# =============================================================================
# def get_neighbours(G: Graph, sol: List[int]):
#     paths = G._shortest_paths
#     size = len(G)
#     neigbours = []
#     neigbours.append(sol[1:])
#     neigbours.append(sol[:-1])
#     for _ in range(2):
#         for i in range(len(sol)-1):
#             while True:
#                 v = np.random.randint(0, size)
#                 if v != sol[i] and v != sol[i+1]:
#                     break
#             iv = paths[sol[i]][v]
#             vj = paths[v][sol[i+1]]
#             insert = iv[1:] + vj[1:-1]
#             neigbours.append(sol[:i+1]+insert[:]+sol[i+1:])
#         for i in range(len(sol)-2-_):
#             diff = 2+_
#             if i != i+diff:
#                 insert = paths[sol[i]][sol[i+diff]][1:-1]
#                 neigbours.append(sol[:i]+insert[:]+sol[i+diff:])
#     return neigbours
# =============================================================================


def fitness(G: Graph, profit_table: np.ndarray, loss_coef: float,
            sol: List[int]):
    profit = 0
    profit_table = profit_table.copy()
    for i in range(len(sol)):
        if i < len(sol) - 1:    # 'i' nie jest ostatnie w rozwiązaniu
            for prof_ix in sol[i+1:]:
                profit += profit_table[sol[i]][prof_ix]
                profit_table[sol[i]][prof_ix] = 0
        if i > 0:               # 'i' nie jest pierwsze w rozwiązaniu
            profit -= loss_coef * G[sol[i-1]][sol[i]]
    return np.round(profit,2)
