from heapq import heappush, heappop
def a_star(G, s, t, h):
    P, Q = {} , [(h(s), None, s)]
    while Q:
        d, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        if u == t: return d - h(t), P
        for v in G[u]:
            w = G[u][v] - h(u) + h(v)
            heappush(Q, (d + w, u, v))
    return inf, None
