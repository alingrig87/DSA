MOD = 101 #fixed modulo. ~sqrt(101) computations. we will probably have two hashes w/ the same value. (~10)
BASE = 27 #random base, chosen at runtime.

s, t = input(), input()
n, m = len(s), len(t)

def conv(ch):
    return ord(ch) - ord('a') + 1

def hash(s: str):
    ans = 0
    for ch in s:
        ans = (ans * BASE + conv(ch)) % MOD
    return ans

#BASE ** (m-1).
Bm1 = 1
for _ in range(m-1):
    Bm1 = Bm1 * BASE % MOD

#O(n + m).
ht = hash(t)
hw = hash(s[:m])
for i in range(n-m+1): #roll O(n-m) times. O(n-m).
    if hw == ht:
        print(f"match at {i}.")
    
    if i < n-m: #roll the hash.
        hw = ((hw - conv(s[i]) * Bm1 % MOD + MOD) * BASE + conv(s[i+m])) % MOD #O(1).