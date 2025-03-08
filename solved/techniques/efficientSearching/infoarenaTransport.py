#infoarena.ro/problema/transport

n, k = 6, 3
v = [7, 3, 2, 3, 1, 4]

def can_do(c, k):
    #if we rent a truck w/ capacity c, can we do at most k visits?
    i = 0
    for _ in range(k):
        rem = c
        while i < n and rem >= v[i]:
            rem -= v[i]
            i += 1
    return i >= n

#print([can_do(c, k) for c in range(max(v), sum(v) + 1)])
l, r = max(v), sum(v)
step = 1 << 30
while step:
    if r - step >= l and can_do(r - step, k):
        r -= step
    step >>= 1

print(r)
