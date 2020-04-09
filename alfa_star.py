import numpy as np
from copy import deepcopy
from simple_queue import Queue
from graph import Graph
from simple_map import Map


def a_star(G:Graph,start:int,stop:int):
    m=np.array(G.matrix_)
    h=np.array(G.H)
    H=G.H
    open=Queue()
    closed=Map(start,len(G))
    for u in G.get_neighbours(start):
        open.add([G[start][u]+H[u][stop],start,u])
    op=open.lst
    cl=closed.dct
    while True:
        f,u,x=open.get()
        g=f-H[x][stop]
        closed[x]=(round(g,2),u)
        for ng in G.get_neighbours(x):
            if ng not in closed:
                open.add((closed[x][0]+G[x][ng]+H[ng][stop],x,ng))
        if x==stop:
            return closed.reconstruct_path(start,stop)
    return -1   