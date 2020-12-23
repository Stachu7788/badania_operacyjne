from taboo_search import taboo_search, fitness
from graph import Graph
import numpy as np
import matplotlib.pyplot as plt
from graph_templates import graph_list
from ast import literal_eval

# =============================================================================
# Graph1 :  vertices: 13, edges: 25
# 
# Graph3 :  vertices: 25, edges: 45
# =============================================================================


G, s0 = graph_list[2]

profit_table = np.round(10 * np.random.rand(len(G),len(G)), 2)
for i in range(len(profit_table)):
    profit_table[i][i] = 0

sol, fit, n_num = taboo_search(G, profit_table, s0)
plt.plot(fit)
