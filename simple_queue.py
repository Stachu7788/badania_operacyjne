import numpy as np
from typing import List, Tuple
from copy import deepcopy
"""
Queue

Przechowuje dane typu (dystans,id_z,id_do)

get() -> Pierwszy element z kolejki
add(list,tuple or queue) -> dodawanie elementu/ów do kolejki
"""


class Queue:
    def __init__(self, arg: List or Tuple = None):
        self.iter = 0
        self.lst = []
        if arg and type(arg) is Queue:
            self.lst = deepcopy(arg.lst)
        if arg and type(arg) is not Queue:
            self.add(arg)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter < len(self):
            self.iter += 1
            return self.lst[self.iter-1]
        if self.iter == len(self):
            raise StopIteration

    def __bool__(self):
        return bool(self.lst)

    def __str__(self):
        ret = ""
        for dst, u, v in self.lst:
            ret += "{:2} -> {:2} : {}\n".format(u, v, dst)
        return ret

    def __len__(self):
        return len(self.lst)

    def __add_one__(self, arg):
        dst, u, v = arg
        if dst == np.inf:
            return None
        if not len(self.lst):
            self.lst.append((dst, u, v))
        else:
            for i in range(len(self)+1):
                if i < len(self.lst):
                    if dst < self.lst[i][0]:
                        self.lst.insert(i, (dst, u, v))
                        break
                elif i == len(self.lst):
                    self.lst.append((dst, u, v))

    def __add_queue__(self, queue):
        for tup in queue:
            self.__add_one__(tup)

    def add(self, arg: List or Tuple or 'Queue'):
        add_opts = {list: getattr(self, '__add_one__'),
                    tuple: getattr(self, '__add_one__'),
                    Queue: getattr(self, '__add_queue__')}
        f = add_opts[type(arg)]
        if f is None:
            raise Exception('Nothing to add')
        f(arg)

    def get(self) -> Tuple[float,int,int]:
        if len(self):
            return self.lst.pop(0)
        else:
            return None
