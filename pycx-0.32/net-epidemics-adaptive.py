# Simple Network Dynamics simulator in Python
#
# *** Network Epidemics with Adaptive Link Cutting ***
#
# Copyright 2008-2013 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import networkx as NX

RD.seed()

populationSize = 500
linkProbability = 0.01
initialInfectedRatio = 0.01
infectionProb = 0.2
recoveryProb = 0.5
linkCuttingProb = 0.1

susceptible = 0
infected = 1

def init():
    global time, network, positions, nextNetwork

    time = 0
    
    network = NX.erdos_renyi_graph(populationSize, linkProbability)

    positions = NX.random_layout(network)

    for i in network.nodes_iter():
        if RD.random() < initialInfectedRatio:
            network.node[i]['state'] = infected
        else:
            network.node[i]['state'] = susceptible

    nextNetwork = network.copy()

def draw():
    PL.cla()
    NX.draw(network,
            pos = positions,
            node_color = [network.node[i]['state'] for i in network.nodes_iter()],
            with_labels = False,
            edge_color = 'c',
            cmap = PL.cm.YlOrRd,
            vmin = 0,
            vmax = 1)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, network, nextNetwork

    time += 1

    for i in network.nodes_iter():
        if network.node[i]['state'] == susceptible:
            nextNetwork.node[i]['state'] = susceptible
            for j in network.neighbors(i):
                if network.node[j]['state'] == infected:
                    if RD.random() < infectionProb:
                        nextNetwork.node[i]['state'] = infected
                        break
                    else: # adaptive link cutting behavior
                        if RD.random() < linkCuttingProb:
                            if nextNetwork.has_edge(i, j):
                                nextNetwork.remove_edge(i, j)
        else:
            if RD.random() < recoveryProb:
                nextNetwork.node[i]['state'] = susceptible
            else:
                nextNetwork.node[i]['state'] = infected

    del network
    network = nextNetwork.copy()

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
