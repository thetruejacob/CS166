# Simple Network Dynamics simulator in Python
#
# *** Network Epidemics: Parameter Sweep Experiments ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import pylab as PL
import random as RD
import scipy as SP
import networkx as NX

RD.seed()

populationSize = 2000
numberOfLinks = 5000
initialInfectedRatio = 0.01
maxTime = 200

susceptible = 0
infected = 1

er_network = 0
ba_network = 1

def networksimulation(networkType, infectionProb, recoveryProb):

    if networkType == er_network:
        linkProbability = float(numberOfLinks) / float(populationSize * (populationSize - 1) / 2)
        network = NX.erdos_renyi_graph(populationSize, linkProbability)
    else:
        network = NX.barabasi_albert_graph(populationSize, numberOfLinks / populationSize)

    for i in network.nodes_iter():
        if RD.random() < initialInfectedRatio:
            network.node[i]['state'] = infected
        else:
            network.node[i]['state'] = susceptible

    nextNetwork = network.copy()

    for time in xrange(maxTime):

        for i in network.nodes_iter():
            if network.node[i]['state'] == susceptible:
                nextNetwork.node[i]['state'] = susceptible
                for j in network.neighbors(i):
                    if network.node[j]['state'] == infected:
                        if RD.random() < infectionProb:
                            nextNetwork.node[i]['state'] = infected
                            break
            else:
                if RD.random() < recoveryProb:
                    nextNetwork.node[i]['state'] = susceptible
                else:
                    nextNetwork.node[i]['state'] = infected
                    
        network, nextNetwork = nextNetwork, network

    return [network.node[i]['state'] for i in network.nodes_iter()].count(infected)

infectionRates = [i * 0.01 for i in xrange(30)]

PL.subplot(1, 2, 1)
result = []
print 'Starting simulations on Erdos-Renyi networks...'
for i in infectionRates:
    print 'Infection rate = ', i
    s = 0
    for k in xrange(5):
        s += networksimulation(er_network, i, 0.5)
    s /= 5.0
    result.append(s)
PL.plot(infectionRates, result)
PL.title("Erdos-Renyi Network")

PL.subplot(1, 2, 2)
result = []
print 'Starting simulations on Barabasi-Albert networks...'
for i in infectionRates:
    print 'Infection rate = ', i
    s = 0
    for k in xrange(5):
        s += networksimulation(ba_network, i, 0.5)
    s /= 5.0
    result.append(s)
PL.plot(infectionRates, result)
PL.title("Barabasi-Albert Network")

PL.show()
