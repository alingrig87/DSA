n = 5

dad = [0] + [i for i in range(n+1)]
size = [0] + [1 for i in range(n+1)]

#we are in a tree (node x). we want to find the root of the tree.
#O(n) -> O(log n).
def getRoot(x):
    #if dad[x] == x:
    #    return x
    ##x and dad[x] are different, but they are in the same tree => they share the same root.
    #return getRoot(dad[x])
    r = x
    while dad[r] != r:
        r = dad[r]
    #x ..... r.
    while x != r:
        prevDad = dad[x]
        dad[x] = r
        x = prevDad
    return r

#a and b are in the same set <=> a and b are in the same tree <=> a and b share the same root of the tree.
#O(n). O(length of a's way to its root + length of b's way to its root) -> O(log n).
def query(a, b):
    return getRoot(a) == getRoot(b)

#want to unite b's set into a's set <=> unite b's tree into a's tree.
#draw an edge from b's tree's root to a's tree's root.
#O(n). O(length of a's way to its root + length of b's way to its root).
#O(log n)
def unite(a, b):
    if query(a, b):
        return
    
    ra = getRoot(a)
    rb = getRoot(b)
    
    if size[ra] < size[rb]:
        ra, rb = rb, ra

    dad[rb] = ra
    size[ra] += size[rb]
    size[rb] = 0