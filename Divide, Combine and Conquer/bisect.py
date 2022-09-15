# This is how to bisect algorithm was written in pthon

def bisect_right(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi) // 2
        if x < a[mid]: hi = mid
        else: lo = mid + 1
    return lo