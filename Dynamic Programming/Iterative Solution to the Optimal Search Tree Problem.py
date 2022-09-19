from collections import defaultdict

def opt_tree(p):
    n = len(p)
    s, e = defaultdict(int), defaultdict(int)
    for l in range(l, n+1):
        for i in range(n-l+1):
            j = i + l
            s[i,j] = s[i,j-1] + p[j-1]
            e[i, j] = min(e[i,r] + e[r+1,j] for r in range(i,j))
            e[i, j] += s[i, j]
    return e[0, n]