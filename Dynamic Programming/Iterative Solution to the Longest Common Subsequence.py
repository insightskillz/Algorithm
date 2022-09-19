def lcs(a, b):
    n, m = len(a), len(b)
    pre, cur = [0]*(n+1), [0]*(n+1)
    for j in range(1, m+1):
        pre, cur = cur, pre
        for i in range(1, n+1):
            if a[i-1] == b[j-1]:
                cur[i] = pre[i-1] + 1
            else:
                cur[i] = max(pre[i], cur[i-1])
    return cur[n]