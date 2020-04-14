import numpy as np
import matplotlib.pyplot as plt

from timeit import default_timer as timer
from copy import deepcopy

from make_matrix import create_matrix
from simple_queue import Queue
from simple_map import Map
from graph import Graph

from dijkstra import dijkstra                #(List[int},float) or Map
from prima import prima                      #(List[Tuple],float)
from alfa_star import a_star                 #(List[int],float)
from bellman_ford import bellman_ford        #(List[int},float) or Map
from floyd_warshall import floyd_warshall    #(List[int},float) or Map
from kruskal import kruskal                  #(List[Tuple],float)




G=Graph(*create_matrix(25,25,30,dst=7))
G.draw()
a = G.succ
path,cst=a_star(G,12,6)
G.draw(path,title="Koszt: {}".format(cst))





##G=Graph(*create_matrix(15,10,4))
#print(len(G.cons_))
#G.draw()
##a=G.x_
#path,cost=a_star(G,12,3)
#G.draw(path)
##print(G)

#con,cost=prima(G)
#G.draw(con,lw=0.6,title="Prima")
#con,cost2=kruskal(G)
#G.draw(con,lw=0.6,title="Kruskal")

#func=[dijkstra,a_star,bellman_ford,floyd_warshall]
#times=[]
#for f in func:
#    start=timer()
#    f(G,27,5)
#    times.append(timer()-start)
#print("Dijkstra:       {}\nA star:         {}\nBellman-Ford:   {}\nFloyd-Warshall: {}".format(*times))
#
#func=[prima,kruskal]
#times=[]
#for f in func:
#    start=timer()
#    f(G)
#    times.append(timer()-start)
#print("Prima:   {}\nKruskal: {}".format(*times))