def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:
            continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)
    return comp