from simple_queue import Queue
from graph import Graph
from simple_map import Map


def a_star(G: Graph, start: int, stop: int):
    H = G.H
    open = G.get_reachable(start)
    closed = Map(start, len(G))
    op=open.lst
    cl=closed.dct
    while True:
        f, u, x = open.get()
        g = f-H[x][stop]
        if closed[x][1] is None:
            for ng in G.get_neighbours(x):
                if ng not in closed:
                    open.add((closed[x][0]+G[x][ng]+H[ng][stop], x, ng))
        if g < closed[x][0]:
            closed[x] = (round(g, 2), u)
        if x == stop:
            return closed.reconstruct_path(start, stop)
