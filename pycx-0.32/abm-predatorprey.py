# Simple ABM simulator in Python
#
# *** Predator Prey Ecosystem ***
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

initialRabbitPopulation = 100
rabbitReproductionRate = 0.1
rabbitPopulationLimit = 500
rabbitNoiseLevel = 2

initialFoxPopulation = 30
foxReproductionRate = 0.5
foxPopulationLimit = 500
foxNoiseLevel = 3
foxHungerLimit = 10

collisionDistance = 2
CDsquared = collisionDistance ** 2
toBeRemoved = -1

def init():
    global time, rabbits, foxes

    time = 0
    
    rabbits = []
    for i in xrange(initialRabbitPopulation):
        rabbits.append([RD.uniform(0, width), RD.uniform(0, height)])

    foxes = []
    for i in xrange(initialFoxPopulation):
        foxes.append([RD.uniform(0, width), RD.uniform(0, height), 0])

def draw():
    PL.cla()
    if rabbits != []:
        x = [ag[0] for ag in rabbits]
        y = [ag[1] for ag in rabbits]
        PL.scatter(x, y, color = 'pink')
    if foxes != []:
        PL.hold(True)
        x = [ag[0] for ag in foxes]
        y = [ag[1] for ag in foxes]
        PL.scatter(x, y, color = 'brown')
        PL.hold(False)
    PL.axis('scaled')
    PL.axis([0, width, 0, height])
    PL.title('t = ' + str(time))

def clip(a, amin, amax):
    if a < amin: return amin
    elif a > amax: return amax
    else: return a

def step():
    global time, rabbits, foxes

    time += 1
    
    # simulate random motion
    for ag in rabbits:
        ag[0] += RD.gauss(0, rabbitNoiseLevel)
        ag[1] += RD.gauss(0, rabbitNoiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)
    for ag in foxes:
        ag[0] += RD.gauss(0, foxNoiseLevel)
        ag[1] += RD.gauss(0, foxNoiseLevel)
        ag[0] = clip(ag[0], 0, width)
        ag[1] = clip(ag[1], 0, height)

    # detect collision and change state
    for i in xrange(len(foxes)):
        foxes[i][2] += 1                      # fox's hunger level increasing
        for j in xrange(len(rabbits)):
            if rabbits[j] != toBeRemoved:
                if (foxes[i][0]-rabbits[j][0])**2 + (foxes[i][1]-rabbits[j][1])**2 < CDsquared:
                    foxes[i][2] = 0           # fox ate rabbit and hunger level reset to 0
                    rabbits[j] = toBeRemoved  # rabbit eaten by fox
        if foxes[i][2] > foxHungerLimit:
            foxes[i] = toBeRemoved            # fox died due to hunger

    # remove "toBeRemoved" agents
    while toBeRemoved in rabbits:
        rabbits.remove(toBeRemoved)
    while toBeRemoved in foxes:
        foxes.remove(toBeRemoved)

    # count survivors' populations
    rabbitPopulation = len(rabbits)
    foxPopulation = len(foxes)

    # produce offspring
    for i in xrange(len(rabbits)):
        if RD.random() < rabbitReproductionRate * (1.0 - float(rabbitPopulation) / float(rabbitPopulationLimit)):
            rabbits.append(rabbits[i][:]) # making and adding a copy of the parent
    for i in xrange(len(foxes)):
        if foxes[i][2] == 0 and RD.random() < foxReproductionRate * (1.0 - float(foxPopulation) / float(foxPopulationLimit)):
            foxes.append(foxes[i][:]) # making and adding a copy of the parent

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
