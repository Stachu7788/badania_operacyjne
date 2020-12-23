from graph import Graph
from dijkstra import dijkstra


x = [2, 6, 0, 9, 5, 2, 6, 0, 4, 9, 6, 10, 2]
y = [0, 0, 1, 2, 3, 4, 5, 6, 6, 6, 8, 9, 10]
C = [(0, 2), (0, 5), (0, 4), (0, 1), (1, 4), (1, 3), (2, 5), (3, 6), (3, 9),
     (4, 5), (8, 12), (8, 10), (4, 6), (4, 8), (5, 7), (5, 8), (6, 8), (6, 9),
     (6, 10), (7, 8), (7, 12), (9, 10), (9, 11), (10, 11), (10, 12)]
s0 = [0, 1, 3, 9, 11, 10, 6, 4, 8, 12, 7, 5, 2, 0, 4, 6, 8, 12]
G = Graph(x, y, C)
G.create_shortest_paths(dijkstra)
graph_list = [(G, s0)]
#   [0, 1,  2, 3,   4, 5,  6,  7,  8, 9, 10, 11,12,13, 14, 15,16,17,18, 19]
x = [15, 4, 3, 16, 19, 10, 11, 1, 19, 0, 10, 6, 12, 8, 6, 6, 16, 14, 2, 20, 9]
y = [3, 6, 12, 19, 5, 13, 0,   1, 13, 9, 17, 2, 8, 9, 20, 14, 9, 14, 17, 16, 5]
C = [(7, 1), (11, 13), (16, 8), (6, 11), (12, 6), (12, 13), (13, 15), (10, 17),
     (14, 18), (14, 10), (14, 15), (15, 5), (5, 12), (5, 17), (3, 17), (19, 8),
     (16, 4), (1, 11), (12, 17), (10, 3), (2, 15), (2, 18), (16, 17), (12, 16),
     (19, 3), (10, 5), (6, 0), (4, 0), (12, 0), (9, 7), (9, 1), (9, 2), (4, 8),
     (8, 17), (0, 16), (1, 2), (1, 13), (15, 10), (20, 11), (20, 13), (20, 12),
     (7, 11), (20, 6)]
G = Graph(x, y, C)
G.create_shortest_paths(dijkstra)
graph_list.append((G, s0))
x = [0,  7,  13,  6,  0,  1,  3, 13,  3,  0,  4,  7,  4,  8,  3, 13, 10, 6,  3,
     14, 10,  7, 13,  0,  1]
y = [11, 11,  10,  4,  3,  1,  4,  2,  1, 14, 10, 14,  6,  8,  7,  5, 12, 8,
     12, 0,  4,  2, 14,  7, 10]
C = [(0, 24), (0, 9), (18, 10), (1, 17), (1, 13), (5, 8), (4, 5), (4, 6),
     (8, 6), (12, 14), (6, 12), (23, 4), (23, 24), (21, 3), (20, 21), (20, 7),
     (7, 19), (2, 22), (2, 16), (11, 1), (10, 14), (20, 15), (12, 17), (15, 7),
     (3, 12), (3, 17), (13, 17), (20, 17), (2, 15), (16, 11), (3, 6), (18, 24),
     (23, 14), (6, 14), (22, 16), (11, 18), (1, 10), (9, 18), (1, 16),
     (13, 20), (21, 8), (10, 24), (10, 17), (13, 16), (19, 21)]
s0 = [17, 13, 20, 15, 7, 19, 21, 8, 5, 4, 6, 3, 17, 12, 14, 23, 24, 0, 9, 18,
      10, 17, 1, 13, 16, 11, 18, 14, 12, 3, 21, 20, 15, 7]
G = Graph(x, y, C)
G.create_shortest_paths(dijkstra)
graph_list.append((G, s0))
