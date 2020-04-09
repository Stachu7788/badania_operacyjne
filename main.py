import numpy as np
import matplotlib.pyplot as plt
import os

from timeit import default_timer as timer
from copy import deepcopy

from make_matrix import make_net_graph
from simple_queue import Queue
from simple_map import Map
from graph import Graph

from dijkstra import dijkstra                #(List[int},float) or Map
from prima import prima                      #(List[Tuple],float)
from alfa_star import a_star                 #(List[int],float)
from bellman_ford import bellman_ford        #(List[int},float) or Map
from floyd_warshall import floyd_warshall    #(List[int},float) or Map
from kruskal import kruskal                  #(List[Tuple],float)


#G=Graph(*make_net_graph(30,20,5))
G.draw(savefig='fig.png')
G.draw(prima(G)[0],savefig='fig2.png')



#G.draw(kruskal(G)[0],title='mst')


#con,cost=prima(G)
#G.draw(con,'r',savefig='fig.png')

#path,cst=a_star(G,11,9)

#func=[dijkstra,a_star,bellman_ford,floyd_warshall]
#times=[]
#for f in func:
#    start=timer()
#    f(G,27,5)
#    times.append(timer()-start)
#print("Dijkstra:       {}\nA star:         {}\nBellman-Ford:   {}\nFloyd-Warshall: {}".format(*times))
#
#
#    