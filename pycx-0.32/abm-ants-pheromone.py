# Simple ABM simulator in Python
#
# *** Ant Aggregation via Pheromone Communication ***
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
populationSize = 3000

evaporationRate = 0.02
diffusionCoefficient = 0.8
hillClimbingProb = 0.95

def init():
    global time, agents, envir, nextenvir

    time = 0
    
    agents = []
    for i in xrange(populationSize):
        newAgent = [RD.randint(0, width - 1), RD.randint(0, height - 1)]
        agents.append(newAgent)

    envir = SP.zeros([height, width])
    for y in xrange(height):
        for x in xrange(width):
            envir[y, x] = RD.random()

    nextenvir = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(envir, cmap = PL.cm.YlOrRd, vmin = 0, vmax = 3)
    PL.axis('image')
    PL.hold(True)
    x = [ag[0] + 0.5 for ag in agents]
    y = [ag[1] + 0.5 for ag in agents]
    PL.scatter(x, y, cmap = PL.cm.bone)
    PL.hold(False)
    PL.title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def step():
    global time, agents, envir, nextenvir

    time += 1

    # diffusion and evaporation of phenomones
    for x in xrange(width):
        for y in xrange(height):
            localAv = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    localAv += envir[(y+dy) % height, (x+dx) % width]
            localAv /= 9.0
            nextenvir[y, x] = envir[y, x] + (localAv - envir[y, x]) * diffusionCoefficient
            nextenvir[y, x] *= (1.0 - evaporationRate)

    envir, nextenvir = nextenvir, envir

    for ag in agents:

        if RD.random() < hillClimbingProb:
            # simulate hill-climbing motion
            maxph = 0
            maxdx = 0
            maxdy = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    tempx = (ag[0]+dx) % width
                    tempy = (ag[1]+dy) % height
                    if maxph < envir[tempy, tempx]:
                        maxph = envir[tempy, tempx]
                        maxdx = dx
                        maxdy = dy
            ag[0] += maxdx
            ag[1] += maxdy
        else:
            ag[0] += RD.randint(-1, 1)
            ag[1] += RD.randint(-1, 1)

        ag[0] = clip(ag[0], 0, width - 1)
        ag[1] = clip(ag[1], 0, height - 1)

        # production of pheromones
        envir[ag[1], ag[0]] += 0.01

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])

