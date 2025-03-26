n = int(input())

#1, 2, ..., n.
whichSet = [0] + [i for i in range(1, n+1)] #wS = [1, 2, 3, 4, 5]
setMembers = [[]] + [[i] for i in range(1, n+1)] #[[], [1], [2], ...]

"""
setMembers[1] = [1]
setMembers[2] = [2]
setMembers[3] = [3]
setMembers[4] = [4]
setMembers[5] = [5]

unite(3, 5) (<-)

setMembers[1] = [1]
setMembers[2] = [2]
setMembers[3] = [3, 5]
setMembers[4] = [4]
setMembers[5] = []


unite(1, 4) (<-)

setMembers[1] = [1, 4]
setMembers[2] = [2]
setMembers[3] = [3, 5]
setMembers[4] = []
setMembers[5] = []

unite(2, 5) (<-)
whichSet = [1, 2, 3, 1, 3].

setMembers[1] = [1, 4]
setMembers[2] = [2, 3, 5]
setMembers[3] = []
setMembers[4] = []
setMembers[5] = []
"""

def query(a, b): #1 <= a, b <= n.
    return whichSet[a] == whichSet[b]

#modify all elements in whichSet[] which are equal to whichSet[b] to be equal to whichSet[a].
#unite b's set into a'set.
#complexity: may be O(n).
#sa = size of a's set.
#sb = size of b's set.
#O(min(sa, sb)). all unites can't take more than O(nlogn).
def unite(a, b):
    if query(a, b):
        return
    
    #want sz(a) >= sz(b).
    if len(setMembers[whichSet[a]]) < len(setMembers[whichSet[b]]):
        a, b = b, a
    
    #sz(a) >= sz(b).
    #unite b's set into a's set.

    wsb = whichSet[b]
    for x in setMembers[wsb]:
        whichSet[x] = whichSet[a]

    setMembers[a].extend(setMembers[wsb])
    setMembers[wsb] = []
    
# print(query(2, 3)) #F
# print(setMembers)
# unite(3, 5)
# print(query(2, 3)) #F
# print(setMembers)
# unite(1, 4)
# print(query(2, 3)) #F
# print(setMembers)
# unite(2, 5)
# print(query(2, 3)) #T.
# print(setMembers)

for i in range(2, n+1):
    unite(i, 1)