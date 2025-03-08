import random

MOD = 10**9 + 7 #fixed modulo. ~sqrt(101) computations. we will probably have two hashes w/ the same value. (~10)
BASE = random.randint(27, MOD-1) #random base, chosen at runtime.

def conv(ch):
    return ord(ch) - ord('a') + 1

s = input()
n = len(s)

def hash(s: str):
    ans = 0
    for ch in s:
        ans = (ans * BASE + conv(ch)) % MOD
    return ans

#BASE ** k-1
base_powers = [1] + [0] * (n - 1)
for i in range(1, n):
    base_powers[i] = base_powers[i-1] * BASE % MOD

ans = 0
step = 1 << 31

starting_index = 0

while step: #O(n log^2 n)
    #check for ans + step.
    if ans + step <= n-1:
        #compute all hashes of length ans + step.
        hashes = [(hash(s[:ans+step]), 0)]
        for i in range(1, n-(ans+step)+1):
            hh = hashes[-1][0]
            hh = ((hh - base_powers[ans + step - 1] * conv(s[i-1]) + MOD) % MOD * BASE + conv(s[i-1+(ans+step)])) % MOD
            hashes.append((hh, i))

        hashes.sort()
        
        i = 1
        while i < n-(ans+step)+1 and hashes[i][0] != hashes[i-1][0]:
            i += 1
            
        if i < n-(ans+step)+1:
            starting_index = hashes[i][1]
            ans += step
            
    step >>= 1

print(f"max length = {ans}, str = {s[starting_index: starting_index + ans]}")