# Simple Network Dynamics simulator in Python
#
# *** Network Growth ***
#
# Copyright 2011-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import networkx as NX
import math as MT

RD.seed()

m = 2

def init():
    global time, network, maxNodeID, positions

    time = 0

    network = NX.Graph()
    network.add_node(0)

    maxNodeID = 0

    positions = NX.random_layout(network)

def draw():
    PL.cla()
    NX.draw(network, pos = positions)
    PL.axis('image')
    PL.title('t = ' + str(time))

def roulette(options, weights):
    weightsum = float(sum(weights))
    if weightsum == 0.0:
        weightsum = 1.0
    probabilities = [float(x)/weightsum for x in weights]
    r = RD.random()
    s = 0.0
    for k in xrange(len(options)):
        s += probabilities[k]
        if r <= s:
            break
    return options[k]

def step():
    global time, network, maxNodeID, positions

    time += 1

    targets = network.degree().keys()
    preferences = [d for d in network.degree().values()]
    # the first "d" could be varied to, e.g., 1, 1/d, d ** 2, etc.

    maxNodeID += 1
    network.add_node(maxNodeID)
    positions[maxNodeID] = SP.array([RD.gauss(0, 0.01), RD.gauss(0, 0.01)])

    for i in xrange(m):
        target = roulette(targets, preferences)
        network.add_edge(maxNodeID, target)

    positions = NX.spring_layout(network, pos = positions, iterations = 2)

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
