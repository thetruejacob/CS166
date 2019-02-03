# A simple simulation of the logistic map in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL

x = 0.1
a = 4.0
tmax = 100

def f(x):
    return a * x * (1 - x)

xdata = [x]
for t in xrange(tmax):
    x = f(x)
    xdata.append(x)

PL.plot(xdata)
PL.show()
