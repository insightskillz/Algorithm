def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
        if R[u] == R[v]:
            R[v] += 1

def kruskal(G):
    E = [(G[u][v], u,v)  for u in G for v in G[u]]
    T = set()
    C, R = {u:U for u in G}, {u:0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, u):
            T.add((u, v))
            union(C, R, u, v)
    return T
