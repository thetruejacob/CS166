# Drawing cobweb plots in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL

# define an iterative map

a = 3.5
def f(x):
    return a * x * (1 - x)

# draw a curve and a reference line

currentValues = [i/100.0 for i in xrange(100 + 1)]
nextValues = map(f, currentValues)

PL.hold(True)
PL.plot(currentValues, nextValues)
PL.plot([0, 1], [0, 1])

# draw a trajectory

x = 0.1
maxTime = 100

resultX = [x]
resultY = [0]

for i in xrange(maxTime):
    resultX.append(x)
    resultY.append(f(x))
    x = f(x)
    resultX.append(x)
    resultY.append(x)

PL.plot(resultX, resultY)
PL.axis('image')
PL.show()
