# A simple numerical integration by the Euler forward method in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL

N = 0.01
t = 0
tmax = 10
dt = 0.0001
r = 1
K = 1

Ndata = [N]
tdata = [t]

def f(n):
    return n + r * n * (1 - n / K) * dt

while t <= tmax:
    N = f(N)
    t = t + dt
    Ndata.append(N)
    tdata.append(t)

PL.plot(tdata, Ndata)
PL.show()
