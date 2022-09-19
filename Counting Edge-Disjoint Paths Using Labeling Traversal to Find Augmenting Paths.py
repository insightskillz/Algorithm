def paths(G,s, t):
    H, M, count = tr(G), set(), 0
    while True:
        Q, P = {s}, {}
        while Q:
            u = Q.pop()
            if u == t:
                count += 1
                break
            forw = (v for v in G[u] if (u, v) not in M)
            back = (v for v in H[u] if (v, u) in M)
            for v in chain(forw, back):
                if v in P:continue
                P[v] = u
                Q.add(v)
        else:
            return count
        while u != s:
            u, v = P[u], u
            if v in G[u]:
                M.add((u,v))
            else:
                M.remove((v, u))