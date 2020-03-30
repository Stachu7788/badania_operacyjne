import numpy as np
from copy import deepcopy
from simple_queue import Queue
from graph import Graph
from simple_map import Map



def best_connection(mat,heu,u,g_u,stop):
    f_min=np.inf
    x=-1
    for id in range(len(mat)):
        if id!=u:
            f=g_u+mat[u][id]+heu[id][stop]
            if f<f_min:
                f_min=f
                x=id
    mat[u][x]=mat[x][u]=np.inf
    return (f_min,u,x)

def a_star(G:Graph,start:int,stop:int):
    mat=deepcopy(G)
    heu=mat.h_
    open=Queue()
    closed=Map(start,len(mat))
    open.add(best_connection(mat,heu,start,0,stop))
    while True:
        f,u,x=open.get()
        g=f-heu[x][stop]
        if x in closed and g<closed[x][0]:
            closed[x]=(round(g,2),u)
        elif x not in closed:
            closed[x]=(round(g,2),u)
        if x==stop:
            return closed.reconstruct_path(start,stop)
        open.add(best_connection(mat,heu,u,closed[u][0],stop))
        open.add(best_connection(mat,heu,x,closed[x][0],stop))
    return -1   