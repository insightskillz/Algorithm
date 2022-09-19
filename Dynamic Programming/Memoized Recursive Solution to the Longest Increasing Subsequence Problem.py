def rec_lis(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <=seq[cur]:
                res = max(res, 1 + L(pre))
            return res
        return max(L(i) for i in range(len(seq)))

#A Basic Iterative Solution to the Longest Increasing Subsequence Problem
def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)
