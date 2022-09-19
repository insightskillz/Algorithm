
from copy import deepcopy

def johnson(G):
    G = deepcopy(G)
    s = object()
    G[s] = {v: 0 for v in G}
    h, _ = bellam_ford(G, s)
    del G[s]
    for u in G:
        for v in G[u]:
            G[u][v] += h[u] - h[v]
    D, P = {}, {}
    for u in G:
        D[u], P[u] = dijkstra(G, u)
        for v in G:
            D[u][v] += h[v] - h[u]
    return D, P