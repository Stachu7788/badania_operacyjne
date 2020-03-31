import numpy as np
from typing import List, Tuple
from matplotlib import pyplot as plt
from simple_queue import Queue
from simple_map import Map
import copy
"""
Graph
draw(*args,**kwargs) -> Rysowanie grafu/połączeń/trasy
get_neighbours(id) -> Lista sąsiadów
get_closest(id) -> Najbliższy sąsiad
get_reachable(id) -> Kolejka sąsiadów
"""
class Graph:
    def __init__(self,M: List[List],*args):
        self.matrix_=M
        self.size_=len(M)
        self.queue_=Queue()
        self.cons_=[]
        if len(args)==3:
            self.h_=args[0]
            self.x_=args[1]
            self.y_=args[2]
        if len(args)==2:
            self.x_=args[0]
            self.y_=args[1]
        for i in range(self.size_):
            for j in range(i+1,self.size_):
                if self.matrix_[i][j]<np.inf:
                    self.cons_.append((i,j))
                    self.queue_.add((M[i][j],i,j))
                   
    def __getitem__(self,index:int):
        return self.matrix_[index]
    
    def __len__(self):
        return self.size_
    
    def __make_connections__(self, cons: List[Tuple]):
        n=len(cons)
        x=np.zeros([2,n]).tolist()
        y=np.zeros([2,n]).tolist()
        for i in range(n):
            x[0][i]=self.x_[cons[i][0]]
            x[1][i]=self.x_[cons[i][1]]
            y[0][i]=self.y_[cons[i][0]]
            y[1][i]=self.y_[cons[i][1]]
        return (x,y)
    
    def __points__(self):
        plt.scatter(self.x_,self.y_,marker='.')
        for i in range(self.size_):
            plt.annotate(i,(self.x_[i],self.y_[i]))
                    
    def draw(self,*args,**kwargs):
        title=kwargs.pop('title',None)
        mode='graph'                            #default mode
        if type(args[0]) is list:
            if type(args[0][0]) is int:
                mode='path'
            elif type(args[0][0]) is tuple:
                mode='connections'
        elif type(args[0]) is Map:
            mode='connections'
            args=(args[0].get_connections(),*args[1:])
        functions= {'graph'      :   getattr(self,'__draw_graph__'),
                    'path'       :   getattr(self,'__draw_path__'),
                    'connections':   getattr(self,'__draw_connections__')}
        titles=    {'graph'      :  "Graf",
                    'path'       :   "Ścieżka",
                    'connections':   "Połączenia"}
        f=functions[mode]
        if not title:
            title=titles[mode]
        f(*args,**kwargs,title=title)
            
    def __draw_graph__(self,*args,**kwargs):
        self.__points__()
        filetitle=kwargs.pop('savefig',None)
        title=kwargs.pop('title')
        x,y=self.__make_connections__(self.cons_)
        plt.plot(x,y,*args,**kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()
        
    def __draw_connections__(self,cons:List[Tuple],*args,**kwargs):
        self.__points__()
        filetitle=kwargs.pop('savefig',None)
        title=kwargs.pop('title')
        x,y=self.__make_connections__(cons)
        plt.plot(x,y,*args,**kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()
        
    def __draw_path__(self,path:List,*args,**kwargs):
        self.__points__()
        filetitle=kwargs.pop('savefig',None)
        title=kwargs.pop('title')
        plt.plot(self.x_[path],self.y_[path],*args,**kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()
        
    def get_queue(self):
        return copy.deepcopy(self.queue_)
    
    def get_neighbours(self,id:int):
        lst=[]
        for i in range(self.size_):
            if self.matrix_[id][i]<np.inf:
                lst.append(i)
        return lst
    
    def get_closest(self,id:int):
        dst=np.inf
        ret=None
        for i in range(self.size_):
            if 0<self.matrix_[id][i]<dst:
                dst=self.matrix_[id][i]
                ret=i
        return ret
    
    def get_reachable(self,id:int):
        q_=Queue()
        for i in range(self.size_):
            if 0<self.matrix_[id][i]<np.inf and id != i:
                q_.add((self.matrix_[id][i],id,i))
        return q_