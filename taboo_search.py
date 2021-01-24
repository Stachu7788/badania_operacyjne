import numpy as np
from typing import List
from data_class import Data


def taboo_search(D: Data):
    sBest = D.s0
    bestCandidate = sBest
    tabuList = []
    tabuList.append(sBest)
    iterations_wo_change = 0
    while iterations_wo_change < 200:
        iterations_wo_change += 1
        sNeighbourhood = get_neighbours(D, bestCandidate)
        bestCandidate = sNeighbourhood[0]
        for sCandidate in sNeighbourhood:
            if(sCandidate not in tabuList and
               fitness(D, sCandidate) > fitness(D, bestCandidate)):
                bestCandidate = sCandidate
        if fitness(D, bestCandidate) > fitness(D, sBest):
            sBest = bestCandidate
            iterations_wo_change = 0
        tabuList.append(bestCandidate)
        D.add_iteration(len(sNeighbourhood), bestCandidate,
                        fitness(D, bestCandidate))
    D.solution(sBest, fitness(D, sBest))
    return sBest


def get_neighbours(D: Data, sol: List[int]):
    G = D.graph
    paths = G.shortest_paths()
    size = len(G)
    neigbours = []
    neigbours.append(sol[1:])
    neigbours.append(sol[:-1])
    # Deletion
    for num in [1, 2, 3]:
        I_ = np.random.randint(1, len(sol)-1-num, int((4-num)/4*len(sol)))
        for i in I_:
            u, v = sol[i], sol[i+num+1]
            insert = paths[u][v][1:-1]
            neigbours.append(sol[:i+1]+insert+sol[i+num+1:])
    # Insertion
    # Single element
    for i in range(len(sol)-1):
        succesors = set(G.get_succesors(sol[i]))
        common = succesors.intersection(G.get_predecessors(sol[i+1]))
        for el in common:
            neigbours.append(sol[:i+1]+[el]+sol[i+1:])
    # Random insertion
    for _ in range(2):
        for i in range(len(sol)-1):
            while True:
                v = np.random.randint(0, size)
                if v != sol[i] and v != sol[i+1]:
                    break
            iv = paths[sol[i]][v]
            vj = paths[v][sol[i+1]]
            insert = iv[1:] + vj[1:-1]
            neigbours.append(sol[:i+1]+insert[:]+sol[i+1:])
    return neigbours


# =============================================================================
# def get_neighbours(D: Data, sol: List[int]):
#     G = D.graph
#     paths = G.shortest_paths()
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

def fitness(data: Data, sol: List[int]):
    profit = 0
    profit_table = data.profit_table.copy()
    for i in range(len(sol)):
        if i < len(sol) - 1:    # 'i' nie jest ostatnie w rozwiązaniu
            for prof_ix in sol[i+1:]:
                profit += profit_table[sol[i]][prof_ix]
                profit_table[sol[i]][prof_ix] = 0
        if i > 0:               # 'i' nie jest pierwsze w rozwiązaniu
            profit -= data.loss_coeficient * data[sol[i-1]][sol[i]]
    return np.round(profit, 2)
