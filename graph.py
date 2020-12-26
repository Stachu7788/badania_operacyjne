import numpy as np
from typing import List, Tuple, Dict
from matplotlib import pyplot as plt
from simple_map import Map
from copy import deepcopy
from simple_queue import Queue

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
get_queue() -> Zwróć kolejkę połączeń
get_succesors(id) -> Sukcesorzy
get_predessesors(id) -> Poprzednicy
get_connections() -> Połączenia [(u do v)]
"""


class Graph:
    def __init__(self, *args):
        self._queueType = Queue
        self._assign_variables(*args)

    def __getitem__(self, index: int):
        return self._matrix[index]

    def __len__(self):
        return self._size
    
    def __str__(self):
        return np.array(self._matrix).__str__()

    def _make_connections(self, cons: List[Tuple]):
        n = len(cons)
        x = np.zeros([2, n]).tolist()
        y = np.zeros([2, n]).tolist()
        for i in range(n):
            x[0][i] = self._x[cons[i][0]]
            x[1][i] = self._x[cons[i][1]]
            y[0][i] = self._y[cons[i][0]]
            y[1][i] = self._y[cons[i][1]]
        return (x, y)

    def _points(self, mark):
        if not mark:
            mark = '.'
        plt.scatter(self._x, self._y, marker=mark)
        for i in range(self._size):
            plt.annotate(self._labels[i], (self._x[i], self._y[i]))

    def _draw_graph(self, *args, **kwargs):
        x, y = self._make_connections(self._cons)
        self._plot(x, y, *args, **kwargs)

    def _draw_connections(self, cons: List[Tuple], *args, **kwargs):
        x, y = self._make_connections(cons)
        self._plot(x, y, *args, **kwargs)

    def _draw_path(self, path: List, *args, **kwargs):
        x=[]
        y=[]
        for i in path:
            x.append(self._x[i])
            y.append(self._y[i])
        self._plot(x, y, *args, **kwargs)

    def _plot(self, x, y, *args, **kwargs):
        if not args:
            args = tuple('b')
        if not kwargs.get('lw'):
            kwargs['lw'] = 0.5
        self._points(kwargs.pop('marker', None))
        filetitle = kwargs.pop('savefig', None)
        title = kwargs.pop('title')
        plt.plot(x, y, *args, **kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()
        
    def _calculate_distances(self, x, y, con):
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

    def _create_shortest_paths(self, fun):
        self._shortest_paths = {}
        for i in range(len(self)):
            self._shortest_paths[i] = {}
            map_: Map = fun(self, i)
            for j in range(len(self)):
                self._shortest_paths[i][j] = map_.reconstruct_path(i, j)[0]

    def _arg_parser(func):
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
            if args and type(args[0]) is list:
                C, args = args[0], args[1:]
            if not M:
                M, H = self._calculate_distances(x, y, C)
            kw_dct = {}
            vars = M, H, x, y, C, L
            for i in range(6):
                if vars[i]:
                    kw_dct[arg_order[i+1]] = vars[i]
            func(self, **kw_dct)
        return wrapper

    def is_directed(self) -> bool:
        return self._dir

    @_arg_parser
    def _assign_variables(self, *args, **dict_args):
        self._matrix = dict_args.pop('M', None)
        if np.array_equal(np.array(self._matrix),np.array(self._matrix).T):
            self._dir = False
        else:
            self._dir = True
        self._H = dict_args.pop('H', None)
        self._x = dict_args.pop('x', None)
        self._y = dict_args.pop('y', None)
        self._size = len(self._matrix)
        self._succ = {}
        self._pred = {}
        self._shortest_paths_created = False
        for i in range(self._size):
            self._succ[i] = []
            self._pred[i] = []
        self._labels = np.arange(0, self._size).tolist()
        self._queue = self._queueType()
        self._cons = dict_args.pop('C', [])
        for i in range(self._size):
            for j in range(i+1, self._size):
                if 0 < self._matrix[i][j] < np.inf:
                    self._succ[i].append(j)
                    self._pred[j].append(i)
                if 0 < self._matrix[j][i] < np.inf:
                    self._succ[j].insert(0, i)
                    self._pred[i].insert(0, j)
        if not self._cons:
            for i in range(self._size):
                for j in range(i+1, self._size):
                    if self[i][j] < np.inf:
                        self._cons.append((i, j))
                        self._queue.add((self[i][j], i, j))
                    if self._dir and self[j][i] < np.inf:
                        self._cons.append((j, i))
                        self._queue.add((self[j][i], j, i))
        else:
            for i, j in self._cons:
                self._queue.add((self._matrix[i][j], i, j))


    def H(self):
        return self._H
    
    def M(self):
        return deepcopy(self._matrix)

    def draw(self, *args, **kwargs):
        if args and not len(args[0]):
            return None
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
        functions = {'graph': getattr(self, '_draw_graph'),
                     'path': getattr(self, '_draw_path'),
                     'connections': getattr(self, '_draw_connections')}
        titles = {'graph': "Graf",
                  'path': "Ścieżka",
                  'connections': "Połączenia"}
        f = functions[mode]
        if not title:
            title = titles[mode]
        f(*args, **kwargs, title=title)

    def random_path(self, n: int):
        path = [np.random.randint(0, len(self))]
        discrete_uniform = {0 : 150, 1: 10, 2: 5, 3: 1, 4: 1, 5: 1, 6: 1}
        vertex_account = len(self) * [0]
        last_occurance = len(self) * [10]
        vertex_account[path[0]] = 1
        while len(path) < n:
            nxt = None
            choices = None
            choices = []
            succ = self.get_succesors(path[-1])
            for v in succ:
                choices += (discrete_uniform[vertex_account[v]] +
                            last_occurance[v]) * [v]
                nxt = np.random.choice(choices)
            path.append(nxt)
            vertex_account[nxt] += 1
            for val in last_occurance:
                val += 1
            last_occurance[nxt] = 0
        return path            

    def create_shortest_paths(self, function):
        if not self._shortest_paths_created:
            try:
                self._create_shortest_paths(function)
                self._shortest_paths_created = True
            except:
                raise Graph_Error("Cannot create shortest paths")

    def shortest_paths(self):
        return self._shortest_paths

    def get_queue(self):
        return deepcopy(self._queue)

    def get_neighbours(self, id: int = None):
        if id is not None:
            return self._succ[id]
        else:
            return self._succ

    def get_succesors(self, id: int = None):
        if id is not None:
            return self._succ[id]
        else:
            return self._succ

    def get_predecessors(self, id: int = None):
        if id is not None:
            return self._pred[id]
        else:
            return self._pred

    def get_connections(self) -> List[tuple]:
        return self._cons

    def get_closest(self, id: int) -> int:
        max_dist = np.inf
        closest = None
        for succ in self._succ[id]:
            if self._matrix[id][succ] < max_dist:
                closest = succ
                max_dist = self._matrix[id][succ]
        return closest

    def get_reachable(self, id: int):
        q = self._queueType()
        for succ in self._succ[id]:
            q.add((self._matrix[id][succ], id, succ))
        return q


class Graph_Error(Exception):
    def __init__(self, message):
        self.message = message
    
