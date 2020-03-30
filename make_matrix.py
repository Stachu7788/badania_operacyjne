import numpy as np

def make_matrix(n):
    array=np.floor(100*np.random.rand(n,n)+1)
    l=np.random.randint(1,n**2/4)
    k=np.random.randint(0,n,(l,2))
    for i in range(n):
        for j in range(i,n):
            if i==j:
                array[i][i]=np.inf
            else:
                array[i][j]=array[j][i]
    for col in k[:]:
        array[col[0]][col[1]]=np.inf
        array[col[1]][col[0]]=np.inf
    return array

def make_net_graph(n,size=100,dist=5):
    while True:
        x=np.random.randint(0,size,size=n)
        y=np.random.randint(0,size,size=n)
        temp=set()
        for i in range(n):
            temp.add((x[i],y[i]))
        if len(temp)==len(x):
            break
    T=np.zeros([n,n])
    for i in range(n):
        T[i][i]=0
        for j in range(i+1,n):
            T[i][j]=T[j][i]=round(np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2),2)
    M=np.where(T[:][:]<=dist,T[:][:],np.inf)
    return (M,T,x,y)