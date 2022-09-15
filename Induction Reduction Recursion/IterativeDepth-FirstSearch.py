def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
       u = Q.pop()
       if u in S: continue
       S.add(u)
       for v in G[u]:
           Q.add(v)
       yield u


class stack(list):
    add = list.append


list(traverse(G, 0, stack))