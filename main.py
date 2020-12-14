import numpy as np
import matplotlib.pyplot as plt

from timeit import default_timer as timer
from copy import deepcopy

from matrix import create_matrix
from simple_queue import Queue
from simple_map import Map
from graph import Graph
from binary_heap import BinaryHeap
from binomial_heap import BinomialHeap

from dijkstra import dijkstra                #(List[int],float) or Map
from prima import prima                      #(List[Tuple],float)
from alfa_star import a_star                 #(List[int],float)
from bellman_ford import bellman_ford        #(List[int],float) or Map
from floyd_warshall import floyd_warshall    #(List[int],float) or Map or
                                             #(List[float],List[int])
from kruskal import kruskal                  #(List[Tuple],float)

# bubble: 1.23


G = Graph(*create_matrix(25,25,30,dst=7))
G.draw()
H = Graph(G.H())
q=H.get_queue()
lst=[]
while q:
    lst.append(q.get())


def test(constructor, lst):
    n=len(lst)
    q=constructor()
    b=constructor()
# =============================================================================
#     try:
#         asd = q._lst
#     except AttributeError:
#         pass
# =============================================================================
    add=timer()
    for tup in lst:
        q.add(tup)
    add=timer()-add
    a=deepcopy(q)
    for _ in range(int(n/2)):
        b.add(a.get())
    get=timer()
    while q:
        q.get()
    get=timer()-get
    merge=timer()
    a.merge(b)
    merge=timer()-merge
    print(f"Add  : {100*add:.4}\nGet  : {100*get:.4}\nMerge: {100*merge:.4}")


print("\nBinomialHeap")
test(BinomialHeap, lst)

print("\nBinaryHeap")
test(BinaryHeap,lst)

print("\nQueue")
test(Queue,lst)

print('\n')
brh = BinaryHeap()
brh_time = timer()
for dst, u, v in lst:
    brh.add([dst, u, v])
brh_time = timer() - brh_time

blh = BinomialHeap()
blh_time = timer()
for dst, u, v in lst:
    blh.add([dst, u, v])
blh_time = timer() - blh_time

sq = Queue()
q_time = timer()
for dst, u, v in lst:
    sq.add([dst, u, v])
q_time = timer()-q_time

print(f"Binary Heap:   {brh_time}\nBinomial Heap: {blh_time}\n" +
      f"Simple Queue:  {q_time}")

# =============================================================================
# M=[[0, 3, 5, np.inf],
#    [2, 0, np.inf, 4],
#    [1, np.inf, 0, 6],
#    [np.inf, 8, 2, 0]]
# M=np.array(M)
# H=Graph(M,[1,2,1,2],[2,2,1,1])
# H.draw()
# 
# 
# path,cost=dijkstra(H,3,0)
# path2,cost2=dijkstra(H,0,3)
# 
# G=Graph(*create_matrix(25,25,30,dst=7))
# G.draw()
# path,cost=bellman_ford(G,5,20)
# G.draw(path,title=f'Koszt: {cost}')
# 
# a=np.random.randint(0,100,[9,9])
# 
# 
# g=Graph(b)
# print(g.cons_)
# 
# 
# 
# #G=Graph(*create_matrix(15,10,4))
# print(len(G.cons_))
# G.draw()
# #a=G.x_
# path,cost=a_star(G,12,3)
# G.draw(path)
# #print(G)
# 
# con,cost=prima(G)
# G.draw(con,lw=0.6,title="Prima")
# con,cost2=kruskal(G)
# G.draw(con,lw=0.6,title="Kruskal")
# 
# func=[dijkstra,a_star,bellman_ford,floyd_warshall]
# times=[]
# for f in func:
#     start=timer()
#     f(G,27,5)
#     times.append(timer()-start)
# print("Dijkstra:       {}\nA star:         {}\nBellman-Ford:   {}\nFloyd-Warshall: {}".format(*times))
# 
# func=[prima,kruskal]
# times=[]
# for f in func:
#     start=timer()
#     f(G)
#     times.append(timer()-start)
# print("Prima:   {}\nKruskal: {}".format(*times))
# =============================================================================
