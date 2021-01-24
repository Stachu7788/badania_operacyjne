from graph import Graph
from typing import List
import numpy as np
import matplotlib.pyplot as plt


class Data:
    def __init__(self, G: Graph, profit_table: np.ndarray,
                 loss_coeficient: int, s0: List[int]):
        self.graph = G
        self.s0 = s0
        self.loss_coeficient = loss_coeficient
        self.profit_table = profit_table
        self.number_of_neighbours_lst = []
        self.best_solution = []
        self.best_fitness = 0
        self.best_candidate_lst = []
        self.best_candidates_fitness_lst = []

    def __getitem__(self, ix: int):
        return self.graph[ix]

    def __str__(self):
        return str(self.best_fitness) + ' : ' + str(self.best_solution)

    def __repr__(self):
        self._calculate()
        return repr(self.info)

    def add_iteration(self, num: int, candidate: List[int], fitness: float):
        self.best_candidate_lst.append(candidate)
        self.number_of_neighbours_lst.append(num)
        self.best_candidates_fitness_lst.append(fitness)

    def solution(self, sol: List[int] = None, fit: float = None):
        if sol is None:
            return self.best_solution
        else:
            self.best_solution = sol
            self.best_fitness = fit
            self._calculate()

    def plot(self):
        plt.plot(self.best_candidates_fitness_lst)

    def _calculate(self):
        self.info = {}
        self.info['Variance'] = np.var(self.best_candidates_fitness_lst)
        temp = np.std(self.best_candidates_fitness_lst)
        self.info['Standard deviation'] = temp
        self.info['Mean'] = np.mean(self.best_candidates_fitness_lst)
        self.info['Median'] = np.median(self.best_candidates_fitness_lst)
        self.info['Number of iterations'] = len(self.best_candidate_lst)
        temp = np.sum(self.number_of_neighbours_lst)
        self.info['Checked solutions number'] = temp
        self.info['Best score'] = self.best_fitness
