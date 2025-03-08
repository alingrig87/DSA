import random

#s = "abbababb"
#t = "bab"
#n, m = len(s), len(t)
n, m = 1000000, 500000
s = 'a' * n
t = ''.join([random.choice(['a', 'b']) for _ in range(m)])

matches = 0
avgComparisons = 0
for i in range(n-m+1):
    j = 0
    while j < m and t[j] == s[i+j]:
        j += 1
    
    avgComparisons += (j+1)
        
    if j >= m:
        #print(f"match starting at index {i}.")
        matches += 1
        
avgComparisons /= (n-m+1)

print(f"matches = {matches}, avgCmp = {avgComparisons}.")