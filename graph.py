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
    def __init__(self,*args):
        self.__assign_variables__(*args)

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
    
    def __points__(self,mark):
        if not mark:
            mark='.'
        plt.scatter(self.x_,self.y_,marker=mark)
        for i in range(self.size_):
            plt.annotate(self.labels[i],(self.x_[i],self.y_[i]))
                    
    def draw(self,*args,**kwargs):
        title=kwargs.pop('title',None)
        mode='graph'                            #default mode
        if args and type(args[0]) is list:
            if type(args[0][0]) is int:
                mode='path'
            elif type(args[0][0]) is tuple:
                mode='connections'
        elif args and type(args[0]) is Map:
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
        x,y=self.__make_connections__(self.cons_)
        self.__plot__(x,y,*args,**kwargs)
        
    def __draw_connections__(self,cons:List[Tuple],*args,**kwargs):
        x,y=self.__make_connections__(cons)
        self.__plot__(x,y,*args,**kwargs)

        
    def __draw_path__(self,path:List,*args,**kwargs):
        x,y=self.x_[path],self.y_[path]
        self.__plot__(x,y,*args,**kwargs)
        
    def __plot__(self,x,y,*args,**kwargs):
        if not args:
            args=tuple('b')
        if not kwargs.get('lw'):
            kwargs['lw']=0.5
        self.__points__(kwargs.pop('marker',None))
        filetitle=kwargs.pop('savefig',None)
        title=kwargs.pop('title')
        plt.plot(x,y,*args,**kwargs)
        plt.title(title)
        if filetitle:
            plt.savefig(filetitle)
        plt.show()
        
    def get_queue(self):
        return copy.deepcopy(self.queue_)
    
    def get_neighbours(self,id:int):
        lst=[]
        for i in range(self.size_):
            if self.matrix_[id][i]<np.inf and id != i: 
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
    
    
    def __calculate_distances__(self,x,y,con):
        if len(x) is not len(y):
            raise Exception("Invalid data")
        else:
            n=len(x)
            H=np.zeros([n,n]).tolist()
            M=(np.inf*np.ones([n,n])).tolist()
            for i in range(n):
                H[i][i]=M[i][i]=0
                for j in range(i+1,n):
                    H[i][j]=H[j][i]=round(np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2),2)
                    if (i,j) in con or (j,i) in con:
                        M[i][j]=M[j][i]=H[i][j]
            return M,H
            
    def arg_parser(func):
        def wrapper(self,*args):
            
            arg_order={1    :   'M',    # Possible inputs:
                       2    :   'H',    # M H x y (l)
                       3    :   'x',    # M x y (l)
                       4    :   'y',    # x y C (l)
                       5    :   'C',    # M (l)
                       6    :   'l'}
            
            for i in range(len(args)):
                if type(args[i]) is np.ndarray:
                    args=*args[:i],args[i].tolist(),*args[i+1:]
            M,H,x,y,C,l=6*[None]
            if type(args[0][0]) is list:   #is first (n,n)
                M,args=args[0],args[1:]
            if args and type(args[0][0]) is list:   #is second (n,n)
                H,args=args[0],args[1:]
            if args and type(args[0][0]) is int:
                x,args=args[0],args[1:]
                y,args=args[0],args[1:]
            if args and type(args[0]) is list and type(args[0][0]) is tuple:
                C,args=args[0],args[1:]
            if args and type(args[0]) is list:
                l,args=args[0],args[1:]
            if not M:
                M,H=self.__calculate_distances__(x,y,C)
            kw_dct={}
            vars=M,H,x,y,C,l
            for i in range(6):
                if vars[i]:
                    kw_dct[arg_order[i+1]]=vars[i]
            func(self,**kw_dct)
                
        return wrapper
            
    @arg_parser
    def __assign_variables__(self,*args,**dict_args):
        self.matrix_=dict_args.pop('M',None)
        self.H=dict_args.pop('H',None)
        self.x_=dict_args.pop('x',None)
        self.y_=dict_args.pop('y',None)
        self.size_=len(self.matrix_)
        self.labels=dict_args.pop('l',None)
        if not self.labels or len(self.labels) != self.size_:
            self.labels=np.arange(0,self.size_).tolist()
        self.queue_=Queue()
        self.cons_=dict_args.pop('C',[])
        if not self.cons_:
            for i in range(self.size_):
                for j in range(i+1,self.size_):
                    if self[i][j]<np.inf:
                        self.cons_.append((i,j))
                        self.queue_.add((self[i][j],i,j))
        else:
            for i,j in self.cons_:
                self.queue_.add((self.matrix_[i][j],i,j))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            