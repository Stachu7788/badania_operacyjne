import numpy as np
from typing import List, Tuple
from matplotlib import pyplot as plt
from simple_queue import Queue
from simple_map import Map
import copy
"""
Graph

Możliwe parametry wejściowe:
    M H x y
    M x y
    x y C
    M              *bez rysowania

draw(*args,**kwargs) -> Rysowanie grafu/połączeń/trasy
    kwargs:
        savefig = str  zapisz figurę jako str
        marker = str  marker dla punktów 
        title = str  tytuł wykresu
get_neighbours(id) -> Lista sąsiadów
get_closest(id) -> Najbliższy sąsiad
get_reachable(id) -> Kolejka sąsiadów
"""


class Graph:
    def __init__(self, *args):
        self.__assign_variables__(*args)

    def __getitem__(self, index: int):
        return self.matrix_[index]

    def __len__(self):
        return self.size_
    
    def __str__(self):
        return np.array(self.matrix_).__str__()

    def __make_connections__(self, cons: List[Tuple]):
        n = len(cons)
        x = np.zeros([2, n]).tolist()
        y = np.zeros([2, n]).tolist()
        for i in range(n):
            x[0][i] = self.x_[cons[i][0]]
            x[1][i] = self.x_[cons[i][1]]
            y[0][i] = self.y_[cons[i][0]]
            y[1][i] = self.y_[cons[i][1]]
        return (x, y)

    def __points__(self, mark):
        if not mark:
            mark = '.'
        plt.scatter(self.x_, self.y_, marker=mark)
        for i in range(self.size_):
            plt.annotate(self.labels[i], (self.x_[i], self.y_[i]))
            
    def H(self):
        return self.H

    def draw(self, *args, **kwargs):
        title = kwargs.pop('title', None)
        mode = 'graph'                            # default mode
        if args and type(args[0]) is list:
            if type(args[0][0]) is int:
                mode = 'path'
            elif type(args[0][0]) is tuple:
                mode = 'connections'
        elif args and type(args[0]) is Map:
            mode = 'connections'
            args = (args[0].get_connections(), *args[1:])
        functions = {'graph': getattr(self, '__draw_graph__'),
                     'path': getattr(self, '__draw_path__'),
                     'connections': getattr(self, '__draw_connections__')}
        titles = {'graph': "Graf",
                  'path': "Ścieżka",
                  'connections': "Połączenia"}
        f = functions[mode]
        if not title:
            title = titles[mode]
        f(*args, **kwargs, title=title)

    def __draw_graph__(self, *args, **kwargs):
        x, y = self.__make_connections__(self.cons_)
        self.__plot__(x, y, *args, **kwargs)

    def __draw_connections__(self, cons: List[Tuple], *args, **kwargs):
        x, y = self.__make_connections__(cons)
        self.__plot__(x, y, *args, **kwargs)

    def __draw_path__(self, path: List, *args, **kwargs):
        x=[]
        y=[]
        for i in path:
            x.append(self.x_[i])
            y.append(self.y_[i])
        self.__plot__(x, y, *args, **kwargs)

    def __plot__(self, x, y, *args, **kwargs):
        if not args:
            args = tuple('b')
        if not kwargs.get('lw'):
            kwargs['lw'] = 0.5
        self.__points__(kwargs.pop('marker', None))
        filetitle = kwargs.pop('savefig', None)
        title = kwargs.pop('title')
        plt.plot(x, y, *args, **kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()

    def get_queue(self):
        return copy.deepcopy(self.queue_)

    def get_neighbours(self, id: int) -> List[int]:
        return self.succ[id]

    def get_succesors(self, id: int) -> List[int]:
        return self.succ[id]

    def get_predecessors(self, id: int) -> List[int]:
        return self.pred[id]

    def get_closest(self, id: int) -> int:
        max_dist = np.inf
        closest = None
        for succ in self.succ[id]:
            if self.matrix_[id][succ] < max_dist:
                closest = succ
                max_dist = self.matrix_[id][succ]
        return closest

    def get_reachable(self, id: int) -> Queue:
        q_ = Queue()
        for succ in self.succ[id]:
            q_.add((self.matrix_[id][succ], id, succ))
        return q_

    def __calculate_distances__(self, x, y, con):
        if len(x) is not len(y):
            raise Exception("Invalid data")
        else:
            n = len(x)
            H = np.zeros([n, n]).tolist()
            M = (np.inf*np.ones([n, n])).tolist()
            for i in range(n):
                H[i][i] = M[i][i] = 0
                for j in range(i+1, n):
                    H[i][j] = H[j][i] = round(np.sqrt((x[i]-x[j])**2 +
                                              (y[i]-y[j])**2), 2)
                    if (i, j) in con or (j, i) in con:
                        M[i][j] = M[j][i] = H[i][j]
            return M, H

    def __arg_parser__(func):
        def wrapper(self, *args):

            arg_order = {1: 'M',    # Possible inputs:
                         2: 'H',    # M H x y (l)
                         3: 'x',    # M x y (l)
                         4: 'y',    # x y C (l)
                         5: 'C',    # M
                         6: 'l'}

            for i in range(len(args)):
                if type(args[i]) is np.ndarray:
                    args = *args[:i], args[i].tolist(), *args[i+1:]
            M, H, x, y, C, L = 6 * [None]
            if type(args[0][0]) is list:            # is 1st (n,n)
                M, args = args[0], args[1:]
            if args and type(args[0][0]) is list:   # is 2nd (n,n) if 1st was
                H, args = args[0], args[1:]
            if args and type(args[0][0]) is int:    # are 2 leading type list
                x, args = args[0], args[1:]
                y, args = args[0], args[1:]
            if args and type(args[0]) is list and type(args[0][0]) is tuple:
                C, args = args[0], args[1:]
            if not M:
                M, H = self.__calculate_distances__(x, y, C)
            kw_dct = {}
            vars = M, H, x, y, C, L
            for i in range(6):
                if vars[i]:
                    kw_dct[arg_order[i+1]] = vars[i]
            func(self, **kw_dct)
        return wrapper

    def is_directed(self) -> bool:
        return self.dir_

    @__arg_parser__
    def __assign_variables__(self, *args, **dict_args):
        m_ = self.matrix_ = dict_args.pop('M', None)
        if np.array_equal(np.array(self.matrix_),np.array(self.matrix_).T):
            self.dir_ = False
        else:
            self.dir_ = True
        self.H = dict_args.pop('H', None)
        self.x_ = dict_args.pop('x', None)
        self.y_ = dict_args.pop('y', None)
        self.size_ = len(self.matrix_)
        s_ = self.succ = {}
        p_ = self.pred = {}
        for i in range(self.size_):
            self.succ[i] = []
            self.pred[i] = []
        self.labels = np.arange(0, self.size_).tolist()
        self.queue_ = Queue()
        self.cons_ = dict_args.pop('C', [])
        for i in range(self.size_):
            for j in range(i+1, self.size_):
                if 0 < self.matrix_[i][j] < np.inf:
                    self.succ[i].append(j)
                    self.pred[j].append(i)
                if 0 < self.matrix_[j][i] < np.inf:
                    self.succ[j].insert(0, i)
                    self.pred[i].insert(0, j)
        if not self.cons_:
            for i in range(self.size_):
                for j in range(i+1, self.size_):
                    if self[i][j] < np.inf:
                        self.cons_.append((i, j))
                        self.queue_.add((self[i][j], i, j))
        else:
            for i, j in self.cons_:
                self.queue_.add((self.matrix_[i][j], i, j))
        
