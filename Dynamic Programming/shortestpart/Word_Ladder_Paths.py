from string import ascii_lowercase as chars
class WordShapce:
    def __init__(self, words):
        self.words = words
        self.M = M = dict()

    def variants(self, wd, words):
        wasl = list(wd)
        for i, c in enumerate(wasl):
            for oc in chars:
                if c == oc: continue
                wasl[i] = oc
                ow = ''.join(wasl)
                if ow in words:
                    yield ow
            wasl[i] = c


    def __getitem__(self, wd):
        if wd not in self.M:
            self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
        return self.M[wd]

    def heuristic(self, u, v):
        return sum(a!=b for a, b in zip(u, v))

    def ladder(self, s, t, h=None):
        if h is None:
            def h(v):
                return self.heuristic(v, t)
        _, P = a_star(self, s, t, h)
        if P is None:
            return [s, None, t]
        u, p = t, []
        while u is not None:
            p.append(u)
            u = P[u]
        p.reverse()
        return P