import random

n = 100000
k = random.randint(0, n)
print(f"expected: {k-1}")

v = [0] * k + [1] * (n-k) #we would like to see k-1.

if v[0] == 1:
    print("-1")
else:
    l, r = 0, n-1
    while r - l > 1: #r - l is divided by 2 (appox) every single pass.
        mid = (l + r) // 2
        if v[mid] == 0:
            l = mid #r >= ans >= mid.
        else:
            r = mid - 1 #l <= ans < mid.
            
    #l == r or l+1 == r (00/01).
    if l+1 == r and v[r] == 0:
        l += 1

    print(l)