from taboo_search import taboo_search, fitness
from graph import Graph
import numpy as np
import matplotlib.pyplot as plt
from graph_templates import graph_list
from ast import literal_eval
from dijkstra import dijkstra

# =============================================================================
# Graph0 :  vertices: 13, edges: 25
# 
# Graph2 :  vertices: 25, edges: 45
# =============================================================================


# =============================================================================
# G, s0 = graph_list[0]
# 
# profit_table = np.round(10 * np.random.rand(len(G),len(G)), 2)
# for i in range(len(profit_table)):
#     profit_table[i][i] = 0
# =============================================================================

# =============================================================================
# ret = taboo_search(G, profit_table, s0, 6)
# # plt.plot(ret[1])
# print(fitness(G, profit_table, 6, ret[0]))
# =============================================================================

a=Graph([1,2,0],[2,0,1],[(1,2)])
a.create_shortest_paths(dijkstra)