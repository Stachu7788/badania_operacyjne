from graph import Graph
import numpy as np
from typing import List


def taboo_search(G: Graph, profit: np.ndarray, s0: List[int]):
    gpl = G, profit, 6
    sBest = s0
    bestCandidate = s0
    fit = [fitness(*gpl, s0)]
    lst = [s0]
    tabuList = []
    tabuList.append(s0)
    for _ in range(500):
        sNeighbourhood = get_neighbours(G, bestCandidate)
        bestCandidate = sNeighbourhood[0]
        for sCandidate in sNeighbourhood:
            if(sCandidate not in tabuList and
               fitness(*gpl, sCandidate) > fitness(*gpl, bestCandidate)):
                bestCandidate = sCandidate
        fit.append(fitness(*gpl, bestCandidate))
        lst.append(bestCandidate)
        if fitness(*gpl, bestCandidate) > fitness(*gpl, sBest):
            sBest = bestCandidate
        tabuList.append(bestCandidate)
    return sBest, fit, lst


def get_neighbours(G: Graph, sol: List[int]):
    paths = G._shortest_paths
    size = len(G)
    neigbours = []
    neigbours.append(sol[1:])
    neigbours.append(sol[:-1])
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
        for i in range(len(sol)-2-_):
            diff = 2+_
            if i != i+diff:
                insert = paths[sol[i]][sol[i+diff]][1:-1]
                neigbours.append(sol[:i]+insert[:]+sol[i+diff:])
    return neigbours


def fitness(G: Graph, profit_table: np.ndarray, loss_coef: float,
            sol: List[int]):
    profit = 0
    profit_table = profit_table.copy()
    for i in range(len(sol)):
        if i < len(sol) - 1:    # i nie jest ostatnie w rozwiązaniu
            for prof_ix in sol[i+1:]:
                profit += profit_table[sol[i]][prof_ix]
                profit_table[sol[i]][prof_ix] = 0
        if i > 0:               # i nie jest pierwsze w rozwiązaniu
            profit -= loss_coef * G[sol[i-1]][sol[i]]
    return profit
