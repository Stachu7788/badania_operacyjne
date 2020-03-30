from


bf=bellman_ford(M,5)
d=dijkstra(M,5)
fw=floyd_warshall(M,5)

dx=np.zeros([2,len(M)])
dy=np.zeros([2,len(M)])
bfx=np.zeros([2,len(M)])
bfy=np.zeros([2,len(M)])
fwx=np.zeros([2,len(M)])
fwy=np.zeros([2,len(M)])

for i in range(len(M)):
    dx[0][i]=x[i]
    dx[1][i]=x[d[i][1]]
    dy[0][i]=y[i]
    dy[1][i]=y[d[i][1]]
    bfx[0][i]=x[i]
    bfx[1][i]=x[bf[i][1]]
    bfy[0][i]=y[i]
    bfy[1][i]=y[bf[i][1]]
    fwx[0][i]=x[i]
    fwx[1][i]=x[fw[i][1]]
    fwy[0][i]=y[i]
    fwy[1][i]=y[fw[i][1]]

plt.scatter(x,y,marker='.')
for i in range(len(M)):
    plt.annotate(i,(x[i],y[i]),(x[i]-0.1,y[i]+0.2))
plt.plot(dx,dy,'r')
plt.title('Dijkstra')
plt.show()

plt.scatter(x,y,marker='.')
for i in range(len(M)):
    plt.annotate(i,(x[i],y[i]),(x[i]-0.1,y[i]+0.2))
plt.plot(bfx,bfy,'g')
plt.title('Bellman-Ford')
plt.show()

plt.scatter(x,y,marker='.')
for i in range(len(M)):
    plt.annotate(i,(x[i],y[i]),(x[i]-0.1,y[i]+0.2))
plt.plot(fwx,fwy,'m')
plt.title('Floyd-Warshall')
plt.show()
    

