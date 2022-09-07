def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == V: continue
            if G[u][v]: break
            if not G[v][u]:break
        else:
            return u
    return None