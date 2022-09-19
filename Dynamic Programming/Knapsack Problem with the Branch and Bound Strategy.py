from __future__ import division
from heapq import heappush, heappop
from itertools import count

def bb_knapsack(w, v, c):
    sol = 0
    n = len(w)
    idxs = list(range(n))
    idxs.sort(key=lambda i: v[i]/w[i],
               revere= True)
    def bound(sw, sv, m):
        if m == n: return sv
        objs = ((v[i], w[i]) for i in idxs[m:])
        for av, aw in objs:
            if sw + aw > c: break
            sw += aw
            sv += av
        return sv + (av/aw)*(c-sw)

    def node(sw, sv, m):
        nonlocal  sol
        if sw > c: return
        if m == n: return
        i = idxs[m]
        ch = [(sw, sv), (sw+w[i], sv +v[i])]
        for sw, sv in ch:
            b = bound(sw, sv, m+1)
            if b > sol:
                yield b, node(sw, sv, m+1)

    num = count()
    Q = [(0, next(num), node(0, 0, 0))]
    while Q:
        _, _, r = heappop(Q)
        for b, u in r:
            heappush(Q, (b, next(num), u))
    return sol