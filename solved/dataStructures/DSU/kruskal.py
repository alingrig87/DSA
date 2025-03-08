from operator import itemgetter

class DSU:
    def __init__(self, n):
        self.dad = [0] + [i for i in range(1, n+1)]
        self.sz = [0] + [1 for i in range(1, n+1)]
        pass
    
    #path compression.
    def getLeader(x): #O(h(n)) = O(log n).
        r = x
        #while r != dad[r]:
        #    r = dad[r]

        return r 
    
    def query(a, b):
        pass
    
    def unite(a, b):
        pass
    
#n nodes, m edges in the graph
#edges = [(a, b, c)] #edge from a to b of cost c.

n = 5
dsu = DSU(n)
edges = []

edges.sort(key = itemgetter(2))

chosenEdges = []
cost = 0
for a, b, c in edges:
    if not dsu.query(a, b):
        cost += c
        dsu.unite(a, b)
        chosenEdges.append((a, b))