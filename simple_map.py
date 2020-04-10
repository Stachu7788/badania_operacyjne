import numpy as np
from typing import List, Tuple
"""
Map

Przechowuje dane typu { klucz : [waga,poprzednik]}

Metody:
get_connections() -> lista połączeń typu (klucz,poprzednik)
reconstruct_path(start,stop) -> lista węzłów w ścieżce
get_closest_from(list) -> najbliższy z list wierzchołek dla startowego
"""


class Map:
    def __init__(self, start: int, num: int):
        self.dct = {}
        for i in range(num):
            self.dct[i] = [np.inf, None]
        self.dct[start] = [0, start]

    def __len__(self):
        return len(self.dct)

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < len(self.dct):
            self.iterator += 1
            return self.dct[self.iterator-1]
        else:
            raise StopIteration

    def __getitem__(self, id: int):
        return self.dct[id]

    def __setitem__(self, id: int, data: Tuple[float, int]):
        self.dct[id] = data

    def __str__(self):
        return self.dct.__str__()

    def __contains__(self, key):
        return self.dct[key][0] < np.inf and self.dct[key][1] is not None

    def items(self):
        return self.dct.items()

    def get_connections(self) -> List[Tuple[int, int]]:
        con = []
        for k, v in self.dct.items():
            con.append((k, v[1]))
        return con

    def get_closest_from(self, lst: List[int]) -> int:
        dst = np.inf
        id = None
        for key, tup in self.dct.items():
            if key in lst and tup[0] < dst:
                dst = self.dct[key][0]
                id = key
        return id

    def reconstruct_path(self, start: int, stop: int) -> List[int]:
        path = []
        dest = stop
        while dest != start:
            path = [dest] + path
            dest = self.dct[dest][1]
        path = [start] + path
        return (path, self.dct[stop][0])
