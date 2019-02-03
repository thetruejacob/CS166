# Simple Network Dynamics simulator in Python
#
# *** Random Walk on a Network ***
#
# Copyright 2010-2013 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import networkx as NX
import random as RD

n = 50
p = 0.1

def init():
    global g, positions, loc
    g = NX.erdos_renyi_graph(n, p, directed = True)
    for nd in g.nodes_iter():
        g.node[nd]['count'] = 0
    positions = NX.spring_layout(g)
    loc = 0

def draw():
    PL.cla()
    NX.draw(g, pos = positions, node_color = [g.node[nd]['count'] for nd in g.nodes_iter()], cmap = PL.cm.Blues, vmin = 0)
    NX.draw_networkx_nodes(g, pos = positions, node_color = 'r', nodelist = [loc])
    
def step():
    global loc
    g.node[loc]['count'] += 1
    if g.neighbors(loc) != []:
        loc = RD.choice(g.neighbors(loc))
    
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
