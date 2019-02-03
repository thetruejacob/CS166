# Simple ABM simulator in Python
#
# *** Random Walk and Diffusion ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

populationSize = 100
noiseLevel = 1

def init():
    global time, agents

    time = 0

    agents = []
    for i in xrange(populationSize):
        newAgent = [RD.gauss(0, 1), RD.gauss(0, 1)]
        agents.append(newAgent)

def draw():
    PL.cla()
    x = [ag[0] for ag in agents]
    y = [ag[1] for ag in agents]
    PL.plot(x, y, 'bo')
    PL.axis('scaled')
    PL.axis([-100, 100, -100, 100])
    PL.title('t = ' + str(time))

def step():
    global time, agents

    time += 1

    for ag in agents:
        ag[0] += RD.gauss(0, noiseLevel)
        ag[1] += RD.gauss(0, noiseLevel)

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
