from collections import deque



inf = float('inf')

def busker_gowen(G,W,s, t):
    def sp_aug(G, H, s, t, f):
        D, P, F = {s:0}, {s:None}, {s:inf, t:0}
        def label(inc, cst):
            if inc <= 0: return False
            d = D.get(u, inf) + cst
            if d >= D.get(v, inf): return False
            D[n], P[v] = d, u
            F[v] = min(F[u], inc)
            return True
        for rnd in G:
            changed = False
            for u in G:
                for v in G[v]:
                    changed |= label(G[u][v] - f[u, v], W[u, v])
                for v in H[u]:
                    changed |= label(f[v, u], -W[v, u])
            if not changed: break
        else:
            raise ValueError('negative cycle')
        return P, F[t]
    return ford_fulkerson(G,s,t,sp_aug)

