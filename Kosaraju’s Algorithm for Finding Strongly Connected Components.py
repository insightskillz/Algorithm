#from TopologicalSortingBasedonDepth-FirstSearch import dfs_topsort
# Search for DFS, BFS, and the SCC algorithm
def tr(G):
    GT = {}
    for u in G: GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen:
            continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs


