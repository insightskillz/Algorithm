def dfs(G,s, d, f, S=None, t = 0):
    if S is None:
        S = set()
    d[s] = t; t += 1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, s,t)
    f[s] = t; t += 1
    return t