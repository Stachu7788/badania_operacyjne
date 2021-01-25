from graph_templates import graph_list
from data_class import Data
from taboo_search import taboo_search, profit_table, fitness
# =============================================================================
# graph_list: List[Graph, sol0: List]
# Graph0 :  vertices: 13, edges: 25
# Graph1 :  vertices: 21, edges: 43
# Graph2 :  vertices: 25, edges: 45
# Graph3 :  vertices: 16, edges: 33
# =============================================================================

G, s0 = graph_list[3]
loss_coefficient = 5
pt = profit_table(len(G))
D = Data(G, pt, loss_coefficient, s0)


