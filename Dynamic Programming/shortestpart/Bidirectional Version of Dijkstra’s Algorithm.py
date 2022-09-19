from  itertools import cycle


def bidir_djkstra(G, s, t):
    Ds, Dt = {}, {}
    forw, back -= idijkstra(G,s), idijkstra(G, t)
    dirs = (Ds, Dt, forw), (Dt, Ds, back)
    try:
        for D, other, step in cycle(dirs):
            v, d = next(step)
            if v in other: break
    except StopIteration: return inf
    m = inf
    for u in Ds:
        for v in G[u]:
            if not v in Dt: continue
            m = min(m, Ds[u] + G[u][v] + Dt[v])
    return m

