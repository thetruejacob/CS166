# How to use NetworkX (2)
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import random as RD
import pylab as PL
import scipy as SP
import networkx as NX

RD.seed()

### creating complex networks

er = NX.erdos_renyi_graph(200, 0.02)

ws = NX.watts_strogatz_graph(200, 4, 0.03)

ba = NX.barabasi_albert_graph(200, 4)

### visualizing networks

PL.subplot(1, 3, 1)
NX.draw(er)
PL.axis('image')
PL.title('Erdos-Renyi')

PL.subplot(1, 3, 2)
NX.draw(ws)
PL.axis('image')
PL.title('Watts-Strogatz')

PL.subplot(1, 3, 3)
NX.draw(ba)
PL.axis('image')
PL.title('Barabasi-Albert')

### obtaining degree distributions

print 'Degrees of all nodes in ba are:'
print NX.degree(ba)

# original degree distribution
hist = NX.degree_histogram(ba)
print 'When binned:'
print hist
PL.figure()
PL.loglog(hist)
PL.title('Original degree distribution')

# complementary cummulative distribution function (CCDF)
ccdf = [sum(hist[k:]) for k in xrange(len(hist))]
print 'Its CCDF:'
print ccdf
PL.figure()
PL.loglog(ccdf)
PL.title('CCDF')

print 'See figures for log-log plots'

### finding important structures

# minimum spanning tree
mst = NX.minimum_spanning_tree(ba)
PL.figure()
PL.title('Minimum spanning tree of ba')
NX.draw(mst)

# K-core
kc = NX.k_core(er)
print 'Nodes in the K-core of er are:'
print kc.nodes()
print 'Size of the K-core: ', kc.number_of_nodes()
PL.figure()
PL.title('K-core of er')
NX.draw(kc)

PL.show()
