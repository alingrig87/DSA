n = 5

#1, 2, ..., n.
whichSet = [0] + [i for i in range(1, n+1)] #wS = [1, 2, 3, 4, 5]

def query(a, b): #1 <= a, b <= n.
    return whichSet[a] == whichSet[b]

#modify all elements in whichSet[] which are equal to whichSet[b] to be equal to whichSet[a].
#unite b's set into a'set.
#O(n) ok.
def unite(a, b):
    wsb = whichSet[b]
    for i in range(1, n+1):
        if whichSet[i] == wsb:
            whichSet[i] = whichSet[a]
            
    #wS = [ ... whichSet[a] ... wsb ..]
    #            b
    
"""
unite(1, 2) change all 2s into 1s.
[1, 2, 3, 2] => [1, 1, 3, 1].
[1, 2, 3, 2] => [1, 1, 3, 2]. whichSet[4] == whichSet[2]
"""