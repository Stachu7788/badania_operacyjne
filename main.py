import numpy as np
import matplotlib.pyplot as plt

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

    

G=Graph(*make_net_graph(20,25,10))
G.draw('c',lw=0.6,savefig='fig.png')


a=bellman_ford(G,5)
con=bellman_ford(G,5)
G.draw(con)

b=str(bellman_ford)
print(b)