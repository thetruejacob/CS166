# Simple ABM simulator in Python
#
# *** Schelling model ***
#
# Copyright 2013 Przemyslaw Szufel & Bogumil Kaminski
# {pszufe, bkamins}@sgh.waw.pl


import matplotlib
from scipy.stats.mstats_basic import threshold
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 50
height = 50
density = 0.8
threshold = 0.7
percent_unhappy = float('nan')
percent_similar = float('nan')
agents = list()
empty = list()


def densityF (val=density):
    """
    The initial population density.
    The parameter change is effective only when model is reset.
    """
    global density
    density = val
    return val

def thresholdF (val=threshold):
    """
    Threshold of changing one's location.
    The parameter can be changed in a running model.
    """
    global threshold
    threshold = val
    return val

def widthF (val=width):
    """
    Grid width.
    The parameter change is effective only when model is reset.
    """
    global width
    width = int(val)
    return val

def heightF (val=height):
    """
    Grid height.
    The parameter change is effective only when model is reset.
    """
    global height
    height = int(val)
    return val

def init():
    """
    Schelling's segregation model (1971)
    """
    global time, config, agents, empty, width, height

    agents = list()
    empty = list()

    time = 0
    
    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < density:
                agents.append((y, x))
                if RD.random() < 0.5:
                    config[y, x] = 1
                else:
                    config[y, x] = -1
            else:
                empty.append((y, x))

def draw():
    PL.cla()
    PL.pcolor(config, vmin = -1, vmax = 1, cmap = PL.cm.RdBu)
    PL.axis('image')
    message = r't = {0}     unhappy: {1}%     similar: {2}%'
    unhappy_pct = round(100*percent_unhappy, 2)
    similar_pct = round(100*percent_similar, 2)
    PL.title(message.format(time, unhappy_pct, similar_pct))

def step():
    global time, config, agents, empty, percent_unhappy, percent_similar

    time += 1
    percent_unhappy = 0
    percent_similar = 0.0

    height, width = config.shape

    sequence = list(range(len(agents)))
    RD.shuffle(sequence)
    for i in sequence:
        agent = agents[i]
        y, x = agent
        state = config[y, x]
        if state == 0:
            continue
        similar = 0
        total = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not ((dx == 0) and (dy == 0)):
                    v = config[(y + dy)%height, (x+dx)%width]
                    if (v != 0):
                        total += 1
                    if (v == state):
                        similar += 1
        if (total == 0):
            percent_similar += 1
        else:
            percent_similar += similar / (1.0*total)
        if (similar < threshold * total):
            percent_unhappy += 1
            newpos = RD.randrange(len(empty))
            new_y, new_x = empty[newpos]
            config[new_y, new_x] = state
            agents[i] = empty[newpos]
            config[y, x] = 0
            empty[newpos] = agent
    percent_unhappy /= (1.0*len(agents))
    percent_similar /= (1.0*len(agents))

import pycxsimulator
pSetters = [densityF,thresholdF,widthF,heightF]
sim = [init,draw,step]
pycxsimulator.GUI(parameterSetters=pSetters,interval=50,stepSize=5).start(func=sim)
