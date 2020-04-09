import numpy as np
from graph import Graph

class Forest:
    """
    Zawiera drzewa typu:
        {id : Set[inne id wierzchołków w drzewie oraz id klucza]}
    """
    def __init__(self, lst):
        self.dct = {}
        for a in lst:
            self.dct[a] = set([a])  

    def is_spannig(self):
        return not bool(len(self.dct)-1) 
# Jeżeli jest więcej niż jedno drzewo w "lesie" to zwraca fałsz

    def connect(self, u, v) -> bool:
        for tree_id in self.dct:
            if u in self.dct[tree_id]:
                u_tree = tree_id
            if v in self.dct[tree_id]:
                v_tree = tree_id
        if u_tree == v_tree:
            return False
        else:
            self.dct[u_tree] = self.dct[u_tree].union(self.dct[v_tree])
                # Union - łączenie ze sobą dwóch zbiorów-"drzew"
            self.dct.pop(v_tree)
            return True


def kruskal(G: Graph):
    M = G.matrix_
    n = len(M)
    L = Forest(np.arange(0, n, 1).tolist())
    con = []
    total = 0
    Q = G.get_queue()
    while not L.is_spannig() and Q:
        dst, u, v = Q.get()
        if L.connect(u, v):
            total += dst
            con.append((u, v))
    return (con, round(total, 2))
        
            

