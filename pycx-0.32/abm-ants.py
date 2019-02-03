# Simple ABM simulator in Python
#
# *** Garbage Collection by Ants ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 50
height = 50

free = 0
carrying = 1

populationSize = 50
garbageProb = 0.8

def init():
    global time, agents, envir

    time = 0

    agents = []
    for i in xrange(populationSize):
        newAgent = [RD.randint(0, width - 1), RD.randint(0, height - 1), free]
        agents.append(newAgent)

    envir = SP.zeros([height, width])
    for y in xrange(height):
        for x in xrange(width):
            if RD.random() < garbageProb:
                state = 1
            else:
                state = 0
            envir[y, x] = state

def draw():
    PL.cla()
    PL.pcolor(envir, cmap = PL.cm.YlOrRd, vmin = 0, vmax = 5)
    PL.axis('image')
    PL.hold(True)
    x = [ag[0] + 0.5 for ag in agents]
    y = [ag[1] + 0.5 for ag in agents]
    s = [ag[2] for ag in agents]
    PL.scatter(x, y, c = s, cmap = PL.cm.binary)
    PL.hold(False)
    PL.title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def step():
    global time, agents, envir

    time += 1
    
    for ag in agents:

        # simulate random motion
        ag[0] += RD.randint(-1, 1)
        ag[1] += RD.randint(-1, 1)
        ag[0] = clip(ag[0], 0, width - 1)
        ag[1] = clip(ag[1], 0, height - 1)

        # simulate interaction between ants and environment
        if envir[ag[1], ag[0]] > 0:
            if ag[2] == free:
                envir[ag[1], ag[0]] -= 1
                ag[2] = carrying
            else:
                envir[ag[1], ag[0]] += 1
                ag[2] = free

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
