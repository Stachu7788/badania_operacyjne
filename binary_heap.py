from typing import List, Tuple
from simple_queue import Queue
import numpy as np


class Node:
    def __init__(self, key: float, *data):
        self.key = key
        self.data = data

    def __str__(self):
        return "{:5.2f} : {}".format(self.key, self.data)

    def get(self):
        return tuple([self.key])+self.data


class BinaryHeap(Queue):
    def __init__(self, arg: List or Tuple = None):
        self._lst = []
        if arg:
            self.add(Node(*arg))

    def __len__(self):
        return len(self._lst)

    def __str__(self):
        ret = ''
        for node in self:
            ret += str(node) + '\n'
        return ret

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
        return bool(len(self))

    def __getitem__(self, index):
        if index > 0:
            return self._lst[index-1]
        else:
            return self._lst[index]

    def __setitem__(self, index, data):
        if index > 0:
            self._lst[index-1] = data
        else:
            self._lst[index] = data

    def add(self, arg: List or Tuple):
        def p(child):   # find parent
            return int((child - child % 2) / 2)
        self._lst.append(Node(*arg))
        child = len(self._lst) - 1
        while child > 1 and self[child].key < self[p(child)].key:
            self[child], self[p(child)] = (self[p(child)], self[child])
            child = p(child)

    def get(self):
        self[1], self[-1] = self[-1], self[1]
        ret = self._lst.pop().get()
        lowest = parent = 1
        while True:
            left = parent * 2
            right = parent * 2 + 1
            if left < len(self) and self[left].key < self[lowest].key:
                lowest = left
            if right < len(self) and self[right].key < self[lowest].key:
                lowest = right
            if lowest != parent:
                self[parent], self[lowest] = (self[lowest], self[parent])
                parent = lowest
            else:
                return ret

    def merge(self, binaryHeap):
        for node in binaryHeap:
            self.add(node.get())
