inf = float('inf')
def relax(W, u, v, D, P):
    d = D.get(u,inf) +W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return true

