# Simple CA simulator in Python
#
# *** Droplet Rule ***
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
initProb = 0.2

def init():
    global time, config, nextConfig

    time = 0

    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            if RD.random() < initProb:
                state = 1
            else:
                state = 0
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y, x]
            numberOfPanicky = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    numberOfPanicky += config[(y+dy)%height, (x+dx)%width]
            if state == 0 and numberOfPanicky >= 4:
                state = 1
            elif state == 1 and numberOfPanicky <= 3:
                state = 0
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
