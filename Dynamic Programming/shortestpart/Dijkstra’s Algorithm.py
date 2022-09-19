from heapq import heappush, heappop

def dijstra(G, s):
    D, P, Q, S = {s:0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S: continue
        S.add(u)
        for v in G[v]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P