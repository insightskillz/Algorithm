from bisect import bisect

def lis(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end): end.append(val)
        else:
            end[idx] = val
        return len(end)