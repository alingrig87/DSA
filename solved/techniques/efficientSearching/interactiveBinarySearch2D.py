#this time we don't know the original interval for x.

import random

x = (random.random() * 2 - 1) * 10 ** random.randint(0, 8)
print(f"x {x}")

def ask(x1, x2):
    return x1 if abs(x1 - x) < abs(x2 - x) else x2

t = ask(-1, 1)
if t == 1:
    #x >= (-1 + 1) / 2 = 0.
    l = 0
    r = 1
    while ask(0, r) != 0:
        r *= 2
else:
    #x <= (-1 + 1) / 2 = 0.
    l = -1
    r = 0
    while ask(l, 0) != 0:
        l *= 2

# l, r = 0, 1
print(f"l {l} r {r}.")
while r - l > 1e-5:
    x1, x2 = (2*l + r) / 3, (l + 2*r) / 3
    if ask(x1, x2) == x1:
        r = (l + r) / 2 #(x1 + x2) / 2
    else:
        l = (l + r) / 2

print(l)
