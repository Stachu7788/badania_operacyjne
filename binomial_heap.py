import numpy as np
from typing import Tuple, List


class Node:
    def __init__(self, key: float, *data):
        self._child = None
        self._sibling = None
        self.key = key
        self.data = data

    def __str__(self):
        return "{:5.2f} : {}".format(self.key, self.data)

    def child(self, *node):
        if node:
            self._child = node[0]
        else:
            return self._child

    def sibling(self, *node):
        if node:
            self._sibling = node[0]
        else:
            return self._sibling

    def get(self):
        return tuple([self.key])+self.data


class BinomialTree:
    def __init__(self, arg: Tuple[float, int, int] or Node, order=0):
        if type(arg) is tuple or type(arg) is list:
            self.root = Node(*arg)
            self.order = 0
        elif type(arg) is Node:
            self.root = arg
            self.root.sibling(None)
            self.order = order

    def __bool__(self):
        return True

    def merge(self, bt):
        if self.order != bt.order:
            return
        if self.root.key <= bt.root.key:
            bt.root.sibling(self.root.child())
            self.root.child(bt.root)
        else:
            self.root.sibling(bt.root.child())
            bt.root.child(self.root)
            self.root = bt.root
        self.order += 1
        return self


class BinomialHeap:
    def __init__(self, arg: Tuple[float, int, int] = None):
        self._dct = {}
        if arg:
            self._dct[0] = BinomialTree(arg)

    def __iter__(self):
        return iter(self._dct)

    def __bool__(self):
        return bool(self._dct)

    def __getitem__(self, index: int):
        return self._dct[index]

    def __setitem__(self, index: int, data: BinomialTree):
        self._dct[index] = data

    def _min_order(self):
        return min(self._dct.keys())

    def _pop_tree(self, order):
        return self._dct.pop(order, None)

    def merge(self, bheap):
        bheap: BinomialHeap
        memory: BinomialTree or None = None
        while memory or bheap:
            if not memory:
                order = bheap._min_order()
                if self._dct.get(order, None):
                    memory = self._pop_tree(order).merge(bheap._pop_tree
                                                          (order))
                else:
                    self[order] = bheap._pop_tree(order)
            elif not bheap or memory.order < bheap._min_order():
                order = memory.order
                if self._dct.get(order, None):
                    memory = self._pop_tree(order).merge(memory)
                else:
                    self[order], memory = memory, None
            else:
                memory.merge(bheap._pop_tree(bheap._min_order()))
        return self

    def add(self, arg: List or Tuple):
        other = BinomialHeap(arg)
        self.merge(other)
        return self

    def insert(self, arg: List or Tuple):
        return self.add(arg)

    def find_min(self):
        val = np.inf
        order = None
        for key, item in self._dct.items():
            if item.root.key < val:
                order = key
                val = item.root.key
        return order

    def delete_root(self, order: int):
        new_heap = BinomialHeap()
        old_tree: BinomialTree = self._pop_tree(order)
        subtree_order: int = old_tree.order - 1
        while subtree_order >= 0:
            subtree_root: Node = old_tree.root.child()
            old_tree.root.child(subtree_root.sibling())
            temp_subtree = BinomialTree(subtree_root, subtree_order)
            new_heap[temp_subtree.order] = temp_subtree
            subtree_order -= 1
        self.merge(new_heap)

    def get(self):
        order = self.find_min()
        dst, u, v = self._dct[order].root.get()
        self.delete_root(order)
        return dst, u, v
