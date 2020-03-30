import numpy as np
from graph import Graph
from simple_queue import Queue

def prima(G:Graph,start=None):
    total=0
    if not start:
        start=0
    tree=set([start])
    con=[]
    Q=G.get_reachable(start)
    while Q:
        dst,u,v=Q.get()
        if v not in tree:
            tree.add(v)
            con.append((u,v))
            total+=dst
            Q.add(G.get_reachable(v))
    return (con,round(total,2)) 
