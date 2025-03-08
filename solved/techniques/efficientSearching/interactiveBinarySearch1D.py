import random

x = random.random() #0 < x < 1.
print(x)

def ask(x1, x2): #which of x1/x2 is closer to x?
    return x1 if abs(x1 - x) < abs(x2 - x) else x2

l, r = 0, 1
while r - l > 1e-5:
    x1, x2 = (2*l + r) / 3, (l + 2*r) / 3
    if ask(x1, x2) == x1:
        r = (l + r) / 2 #(x1 + x2) / 2
    else:
        l = (l + r) / 2

print(l)    
