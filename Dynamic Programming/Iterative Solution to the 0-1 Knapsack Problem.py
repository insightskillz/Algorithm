def knapsack(w, v, c):
    n = len(w)
    m = [[0]*(c+1) for i in range(n+1)]
    p = [[False]*(c+1) for i in range(n+1)]
    for k in range(1, n+1):
        i = k-1
        for r in range(1,c+1):
            m[k][r] = drop = m[k-1][r]
            if w[i] > r: continue
            keep = v[i] + m[k-1][r-w[i]]
            m[k][r] = max(drop, keep)
            p[k][r] = keep > drop
    return m, p