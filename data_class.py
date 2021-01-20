from graph import Graph
from typing import List
import numpy as np


class Data:
    def __init__(self, G: Graph, profit_table: np.ndarray,
                 loss_coeficient: int, s0: List[int]):
        self.graph = G
        self.s0 = s0
        self.loss_coeficient = loss_coeficient
        self.profit_table = profit_table

    def __get__(self, ix: int):
        return self.graph[ix]
