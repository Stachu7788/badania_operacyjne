import numpy as np
from typing import List,Tuple
from copy import deepcopy
"""
Queue
get() -> Pierwszy element z kolejki
add(list,tuple or queue) -> dodawanie elementu/ów do kolejki
"""


class Queue:
    def __init__(self, arg: List or Tuple = None):
        self.size=0
        self.iter=0
        self.lst=[]             #List[Tuple(dst,u,v)]
        if arg and type(arg) is Queue:
            self.lst=deepcopy(arg.lst)
            self.size=arg.size
        if arg and type(arg) is not Queue:
            self.add(arg)
        
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.iter<self.size:
            self.iter+=1
            return self.lst[self.iter-1]
        if self.iter==self.size:
            raise StopIteration
            
    def __bool__(self):
        return bool(self.lst)
    
    def __print__(self):
        for dst,a,b in self.lst:
            print("{} -> {} : {}".format(a,b,dst))
        print("Size: {}    Len: {}".format(self.size,len(self.lst)))
        
    def __add_one__(self,arg):             #[dist,u_id,v_id]   
        dst,u,v=arg
        if dst==np.inf:
            return None
        if self.size:
            for i in range(self.size+1):
                if i<self.size:
                    if dst<self.lst[i][0]:
                        self.lst.insert(i,(dst,u,v))
                        self.size+=1
                        break
                elif i==self.size:
                    self.lst.append((dst,u,v))
                    self.size+=1
        if not self.size:
            self.lst.append((dst,u,v))
            self.size+=1
    
    def __add_queue__(self,queue):
        for tup in queue:
            self.__add_one__(tup)
        
    def add(self,arg: List or Tuple or 'Queue'):
        add_opts={list:     getattr(self,'__add_one__'),
                  tuple:    getattr(self,'__add_one__'),
                  Queue:    getattr(self,'__add_queue__')}
        f=add_opts[type(arg)]
        if f is None:
            raise Exception('Nothing to add')
        f(arg)
        
        
    def get(self):
        if self.size:
            self.size-=1
            return self.lst.pop(0)
        else:
            return None
            
    def __str__(self):
        ret=""
        for dst,u,v in self.lst:
            ret+="{:2} -> {:2} : {}\n".format(u,v,dst)
        return ret
    