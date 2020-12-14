import numpy as np
from typing import List, Tuple
"""
Queue

Przechowuje dane typu (dystans,id_z,id_do)

get() -> Pierwszy element z kolejki
add(list,tuple or queue) -> dodawanie elementu/ów do kolejki
"""


class Queue:
    def __init__(self, arg: List or Tuple = None):
        self._lst = []
        self._add_opts = {list: getattr(self, '_add_one'),
                          tuple: getattr(self, '_add_one'),
                          Queue: getattr(self, '_add_queue')}
        if arg:
            self.add(arg)

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter < len(self._lst):
            ret = self._lst[self._iter]
            self._iter += 1
            return ret
        else:
            raise StopIteration

    def __bool__(self):
        return bool(self._lst)

    def __str__(self):
        ret = ""
        for dst, u, v in self:
            ret += "{:2} -> {:2} : {}\n".format(u, v, dst)
        return ret

    def __len__(self):
        return len(self._lst)

    def _add_one(self, arg):
        dst, u, v = arg
        if dst == np.inf:
            return None
        if not len(self._lst):
            self._lst.append((dst, u, v))
        else:
            i = 0
            j = len(self._lst) - 1 
            while i < j-1:
                mid = (j + i) // 2
                if self._lst[mid][0] < dst:
                    i = mid
                else:
                    j = mid
            if self._lst[j][0] < dst:
                j += 1
            self._lst.insert(j,(dst, u, v))
# =============================================================================
#             for i in range(len(self)+1):
#                 if i < len(self._lst):
#                     if dst < self._lst[i][0]:
#                         self._lst.insert(i, (dst, u, v))
#                         break
#                 elif i == len(self._lst):
#                     self._lst.append((dst, u, v))
# =============================================================================

    def _add_queue(self, queue):
        for tup in queue:
            self._add_one(tup)

    def add(self, arg: List or Tuple or 'Whatever'):
        f = self._add_opts[type(arg)]
        if f is None:
            raise Exception('Nothing to add')
        f(arg)

    def get(self) -> Tuple[float, int, int]:
        if len(self):
            return self._lst.pop(0)
        else:
            return None

    def merge(self, queue):
        self.add(queue)
