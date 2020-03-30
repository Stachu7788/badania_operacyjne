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

    
#
#G=Graph(*make_net_graph(20,25,10))
#G.draw('c',lw=0.6,savefig='fig.png')


a,b=15,6
p1,c1=dijkstra(G,a,b)
p2,c2=a_star(G,a,b)
p3,c3=bellman_ford(G,a,b)
p4,c4=floyd_warshall(G,a,b)
for p,c in ((p1,'g'),(p2,'k'),(p3,'r'),(p4,'m')):
    G.draw(p,c,lw=0.7)



con,cost=prima(G)
con2,cost2=kruskal(G)
G.draw(con,'m',lw=0.5,title='prima')
G.draw(con2,'r',lw=0.5,title='kruskal')
print(G[18][10])

