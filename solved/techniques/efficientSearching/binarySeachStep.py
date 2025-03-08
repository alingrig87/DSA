import random
import math

n = 100000
k = n #random.randint(0, n)
print(f"expected: {k}")

v = [0] * k + [1] * (n-k) #we would like to see k-1.

ans = n
step = 1 << 30 #1 << int(math.log2(n + 1))

while step > 0:
    if ans - step >= 0 and v[ans - step] == 1: #step >= 1. >= ans + 1 >= 0.
        ans -= step
    step >>= 1

print(ans)