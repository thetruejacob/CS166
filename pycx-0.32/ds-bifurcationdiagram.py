# Drawing bifurcation diagrams in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL

# define an iterative map

def f(x):
    return a * x * (1 - x)

# draw a bifurcation diagram

x0 = 0.1
samplingStartTime = 1000
sampleNumber = 100

resultA = []
resultX = []

a = 0
da = 0.005

while a <= 4.0:
    x = x0
    for t in xrange(samplingStartTime):
        x = f(x)
    for t in xrange(sampleNumber):
        x = f(x)
        resultA.append(a)
        resultX.append(x)
    a += da

PL.plot(resultA, resultX, 'bo')
PL.show()
