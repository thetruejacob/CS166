# Simple ABM simulator in Python
#
# *** Diffusion-Limited Aggregation ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 100
height = 100
populationSize = 1000
noiseLevel = 1
collisionDistance = 2
CDsquared = collisionDistance ** 2
toBeRemoved = -1

def init():
    global time, free, fixed

    time = 0
    
    free = []
    for i in xrange(populationSize - 1):
        free.append([RD.uniform(0, width), RD.uniform(0, height)])

    fixed = []
    fixed.append([width / 2, height / 2])

def draw():
    PL.cla()
    if free != []:
        x = [ag[0] for ag in free]
        y = [ag[1] for ag in free]
        PL.scatter(x, y, color = 'cyan')
    if fixed != []:
        PL.hold(True)
        x = [ag[0] for ag in fixed]
        y = [ag[1] for ag in fixed]
        PL.scatter(x, y, color = 'blue')
        PL.hold(False)
    PL.axis('scaled')
    PL.axis([0, width, 0, height])
    PL.title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def step():
    global time, free, fixed

    time += 1

    # simulate random motion
    for ag in free:
        ag[0] += RD.gauss(0, noiseLevel)
        ag[1] += RD.gauss(0, noiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    # detect collision and change state
    for i in xrange(len(free)):
        for j in xrange(len(fixed)):
            if (free[i][0]-fixed[j][0])**2 + (free[i][1]-fixed[j][1])**2 < CDsquared:
                fixed.append(free[i])
                free[i] = toBeRemoved
                break

    # remove "toBeRemoved" free particles
    while toBeRemoved in free:
        free.remove(toBeRemoved)

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
