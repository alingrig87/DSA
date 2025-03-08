import random

MOD = 10**9 + 7 #fixed modulo. ~sqrt(101) computations. we will probably have two hashes w/ the same value. (~10)
BASE = random.randint(27, MOD-1) #random base, chosen at runtime.

def conv(ch):
    return ord(ch) - ord('a') + 1

s = input()
k = int(input())
n = len(s)

def hash(s: str):
    ans = 0
    for ch in s:
        ans = (ans * BASE + conv(ch)) % MOD
    return ans

#BASE ** k-1
Bk1 = 1
for _ in range(k-1):
    Bk1 = Bk1 * BASE % MOD

hashes = [(hash(s[:k]), 0)]

for i in range(1, n-k+1):
    hh = hashes[-1][0]
    hh = ((hh - Bk1 * conv(s[i-1]) + MOD) % MOD * BASE + conv(s[i-1+k])) % MOD
    hashes.append((hh, i))
    
hashes.sort()
print(hashes)

print(hashes[0][1], end = ' ')
ans = 1

for i in range(1, n-k+1):
    if hashes[i][0] != hashes[i-1][0]:
        print(hashes[i][1], end = ' ')
        ans += 1

print()
print(ans)