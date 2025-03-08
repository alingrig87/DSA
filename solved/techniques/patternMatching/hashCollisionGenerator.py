import random

MOD = 10 ** 9 + 7 #fixed modulo. ~sqrt(101) computations. we will probably have two hashes w/ the same value. (~10)
BASE = 27 #random base, chosen at runtime.

def conv(ch):
    return ord(ch) - ord('a') + 1

def hash(s: str):
    ans = 0
    for ch in s:
        ans = (ans * BASE + conv(ch)) % MOD
    return ans

n = 9
hashes = {}

while True:
    s = ''.join([random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) for _ in range(n)])
    hs = hash(s)
    
    if hs in hashes:
        print(f"{s} and {hashes[hs]} collide with the hash {hs} (generated {len(hashes) + 1} hashes).")
        break

    hashes[hs] = s