import numpy as np
import matplotlib.pyplot as plt
import random

def f(temp):
    return -0.5 * (temp - 23) ** 2 + 7 * temp - 32

xs = np.linspace(-15, 50, 1000)

l, r = -15, 50
iters = 0
pts_l, pts_r = [], []
while r - l > 1e-5:
    pts_l.append(l)
    pts_r.append(r)
    p1, p2 = (2*l + r) / 3, (l + 2*r) / 3
    if f(p1) < f(p2):
        l = p1
    else:
        r = p2
    iters += 1
        
print(iters)

plt.plot(xs, [f(x) for x in xs])
plt.scatter([l], [f(l)])

plt.scatter(pts_l, [f(l) for l in pts_l], c = 'g')
plt.scatter(pts_r, [f(r) for r in pts_r], c = 'r')

plt.show()