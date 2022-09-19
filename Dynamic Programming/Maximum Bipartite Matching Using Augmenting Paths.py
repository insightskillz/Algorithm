from collections import defaultdict
from itertools import chain

def match(G, X, Y):
    H = tr(G)
    S, T, M =set(X), set(Y), set()
    while S:
        s = S.pop()
        Q, P = {s}, {}
        while Q:
            u = Q.pop()
            if u in T:
                T.remove(u)
                break
            forw = (v, for c in G[u] if (u,v) not in M)
            back = (v for v in H[u] if (v, u) in M)
            for v in chain(forw, back):
                if v in P: continue
                P[v] = u
                Q.add(v)
        while u != s:
            u, v = P[u], u
            if v in G[u]:
                M.add((u,v))

            else:
                M.remove((v,u))
    return M