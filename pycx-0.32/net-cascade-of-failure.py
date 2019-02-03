# Simple Network Dynamics simulator in Python
#
# *** Cascade of Failure ***
#
# Copyright 2010-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
import random as RD
import math as MT

functioning = 1
failed = 0

capacity = 1.0
maxInitialLoad = 0.8

def init():
    global time, network, positions, nextNetwork

    time = 0

    network = NX.watts_strogatz_graph(200, 4, 0.01)
    for nd in network.nodes_iter():
        network.node[nd]['state'] = functioning
        network.node[nd]['load'] = RD.random() * maxInitialLoad
    network.node[RD.choice(network.nodes())]['load'] = 2.0 * capacity

    positions = NX.spring_layout(network)

    nextNetwork = network.copy()

def draw():
    PL.cla()
    NX.draw(network, with_labels = False, pos = positions,
            cmap = PL.cm.jet, vmin = 0, vmax = capacity,
            node_color = [network.node[nd]['load'] for nd in network.nodes_iter()])
    PL.title('t = ' + str(time))

def step():
    global time, network, nextNetwork

    time += 1

    for nd in network.nodes_iter():
        if network.node[nd]['state'] == functioning:
            ld = network.node[nd]['load']
            nextNetwork.node[nd]['load'] = ld
            if ld > capacity:
                nextNetwork.node[nd]['state'] = failed
                nbs = [nb for nb in network.neighbors(nd) if network.node[nb]['state'] == functioning]
                if len(nbs) > 0:
                    loadDistributed = ld / len(nbs)
                    for nb in nbs:
                        nextNetwork.node[nb]['load'] += loadDistributed

    network, nextNetwork = nextNetwork, network

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
