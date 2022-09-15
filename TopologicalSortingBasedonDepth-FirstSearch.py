def dfs_topsort(G):
    S, res = set(), []
    def recurse(u):
       if u in S: return
       S.add(u)
       for v in G[u]:
           recurse(v)
       res.append(u)
       for u in G:
           recurse(u)
       res.reverse()
       return res
    

