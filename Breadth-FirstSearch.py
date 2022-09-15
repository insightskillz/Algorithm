from collections import deque
def dfs(G, s):
    P, Q = {s : None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[v]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P
