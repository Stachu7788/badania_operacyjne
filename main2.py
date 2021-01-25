from taboo_search import taboo_search, profit_table
from graph import Graph
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

G, s0 = graph_list[3]
pt = profit_table(len(G))
D = Data(G, pt, 10, s0)
ret = taboo_search(D)



