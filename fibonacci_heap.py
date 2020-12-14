import numpy as np
from typing import Tuple, List


class Node:
    def __init__(self, key: float, *data):
        self.key = key
        self.data = data
        self._parent = None
        self._child = None
        self._left = self
        self._right = self
        self.children = 0

    def __str__(self):
        return "{:5.2f} : {}".format(self.key, self.data)

    def __bool__(self):
        return True

    def __iter__(self):
        self._current = self
        return self

    def __next__(self):
        if self._current is not None:
            ret = self._current
            self._current = self._current.right()
            if self._current == self:
                self._current = None
            return ret

    def get(self):
        return tuple([self.key])+self.data

    def left(self, other=None):
        if other:
            self._left = other
        return self._left

    def right(self, other=None):
        if other:
            self._right = other
        return self._right

    def child(self, other=None):
        if other:
            self._child = other
        return self._child

    def parent(self, other=None):
        if other:
            self._parent = other
        return self._parent

    def connect(self, right):
        old_right: Node = self._right
        self.right(right)
        right.left(self)
        right.right(old_right)
        old_right.left(right)
        self._parent.children += 1

    def disconnect(self):
        self._right.left(self._left)
        self._left.right(self._right)
        self.right(None)
        self.left(None)
        self._parent.children -= 1
        return self._child


class FibonacciHeap:
    def __init__(self, tup: List or Tuple = None):
        self.roots = 0
        if tup:
            self.add(tup)
        else:
            self._root = None

    def root(self, node=None):
        if node:
            self._root = node
        return self._root

    def add(self, arg: List or Tuple):
        self.merge(FibonacciHeap(arg))

    def merge(self, fheap):
        fheap = FibonacciHeap()
        if not self.roots:
            self.root(fheap.root())
            self.roots = fheap.roots
        else:
            self.roots += fheap.roots
            self._root.connect(fheap.root())
            self._root = min(self.root(), fheap.root(),
                             key=lambda node: node.key)

    def get(self):
        root: Node = self._root
        for child in root.child:
            self.add(child)
