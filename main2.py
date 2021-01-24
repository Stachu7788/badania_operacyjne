from taboo_search import taboo_search, fitness
from graph import Graph
import numpy as np
import matplotlib.pyplot as plt
from graph_templates import graph_list
from ast import literal_eval
from dijkstra import dijkstra
from data_class import Data

# =============================================================================
# Graph0 :  vertices: 13, edges: 25
# Graph1 :  vertices: 21, edges: 43
# Graph2 :  vertices: 25, edges: 45
# =============================================================================


# =============================================================================
# G, s0 = graph_list[0]
# 
# profit_table = np.round(10 * np.random.rand(len(G), len(G)), 2)
# for i in range(len(profit_table)):
#     profit_table[i][i] = 0
# =============================================================================
D = Data(G, profit_table, 10, s0)


ret = taboo_search(D)

print(D.info)


