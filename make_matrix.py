import numpy as np
"""
n - liczba wierzchołków
size - rozmiar siatki (size x size)
dist - maksymalna odległość między wierzchołkami by te się połączyły
"""


def create_matrix(n, size=100, dist=5):
    while True:
        x = np.random.randint(0, size, size=n)
        y = np.random.randint(0, size, size=n)
        temp = set()
        for i in range(n):
            temp.add((x[i], y[i]))
        if len(temp) == len(x):
            break
    T = np.zeros([n, n])
    for i in range(n):
        T[i][i] = 0
        for j in range(i+1, n):
            T[i][j] = T[j][i] = round(np.sqrt((x[i]-x[j])**2 +
                                      (y[i]-y[j])**2), 2)
    M = np.where(T[:][:] <= dist, T[:][:], np.inf)
    return (M, T, x, y)
