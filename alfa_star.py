from simple_queue import Queue
from graph import Graph
from simple_map import Map


def a_star(G: Graph, start: int, stop: int):
    H = G.H
    open = Queue()
    for succ in G.get_succesors(start):
        open.add([G[start][succ]+H[succ][stop], start, succ])
    closed = Map(start, len(G))
    while True:
        f, u, x = open.get()
        g = f-H[x][stop]
        if g < closed[x][0]:
            closed[x] = (round(g, 2), u)
            for ng in G.get_succesors(x):
                if ng not in closed:
                    open.add((closed[x][0]+G[x][ng]+H[ng][stop], x, ng))
        if x == stop:
            return closed.reconstruct_path(start, stop)
