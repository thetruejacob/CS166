# Drawing phase space of the Lotka-Volterra model by the Euler forward method in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL

a = 1.0
b = 0.1
c = 1.0
d = 0.1
dt = 0.01

def update(x, y):
    return (
        x + (- a * x * y + b * x) * dt,
        y + (c * x * y - d * y) * dt
        )

x0 = 0.1
while x0 <= 1:
    y0 = 0.1
    while y0 <= 1:
        t = 0
        x = x0
        y = y0
        tdata = [t]
        xdata = [x]
        ydata = [y]
        while t < 100:
            t = t + dt
            (x, y) = update(x, y)
            tdata.append(t)
            xdata.append(x)
            ydata.append(y)
        PL.plot(xdata, ydata)
        y0 += 0.1
    x0 += 0.1

PL.axis('image')
PL.show()


