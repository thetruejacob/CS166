## PyCX 0.3 Realtime Visualization Template
## 
## Written by:
## Chun Wong
## email@chunwong.net
##
## Revised by:
## Hiroki Sayama
## sayama@binghamton.edu
##
## "parameterSetters" added by:
## Przemyslaw Szufel & Bogumil Kaminski
## {pszufe, bkamins}@sgh.waw.pl
##
## Copyright 2012 Chun Wong & Hiroki Sayama
## Copyright 2013 Przemyslaw Szufel & Bogumil Kaminski
##

## NOTE: To run your simulation code based on this template, you need
## to have the "pycxsimulator.py" file in the same folder.


# keep the following two lines as is
import matplotlib
matplotlib.use('TkAgg')

##=====================================
## Section 1: Import Modules
##=====================================

# i.e., import pylab as PL

##=====================================
## Section 2: Define Model Parameters
##=====================================

# i.e., n = 10000, RD.seed(), etc.

##=====================================
## Section 3: Define Three Functions
##=====================================

def init():
    # initialize system states
    # use 'global' to define global variables
    
def draw():
    # visualize system states using pylab functions
    # use PL.cla() to clear axis before drawing if needed
    # set title or other related visualizations if needed

def step():
    # update system states for one discrete time step
    # use 'global' to modify global variables

##=====================================
## Section 4: [Optional] Create Setter/Getter Functions for Model Parameters
##=====================================

def setSomeParameter (newValue=someParameter):
    """ The comment will appear in GUI control """
    global someParameter
    someParameter = newValue
    return someParameter

##=====================================
## Section 5: Import and Run GUI
##=====================================

import pycxsimulator
pycxsimulator.GUI(title='My Simulator',interval=0, parameterSetters = []).start(func=[init,draw,step])
# 'title', 'interval' and 'parameterSetters' are optional
