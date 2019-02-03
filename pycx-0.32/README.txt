######################################################################
######################################################################
##
## PyCX 0.32
## Complex Systems Simulation Sample Code Repository
##
## 2008-2016 (c) Copyright by Hiroki Sayama
## 2012 (c) Copyright by Chun Wong & Hiroki Sayama
##          Original GUI module and simulation models
## 2013 (c) Copyright by Przemyslaw Szufel & Bogumil Kaminski
##          Extensions to GUI module, some revisions
## All rights reserved.
##
## See LICENSE.txt for more details of license information.
##
## Send any correspondences to:
##   Hiroki Sayama, D.Sc.
##   Director, Center for Collective Dynamics of Complex Systems
##   Associate Professor, Department of Systems Science and Industrial Engineering
##   Binghamton University, State University of New York
##   P.O. Box 6000, Binghamton, NY 13902-6000, USA
##   Tel: +1-607-777-3566
##   Email: sayama@binghamton.edu
##
## http://pycx.sf.net/
##
######################################################################
######################################################################


1. What is PyCX?

The PyCX Project aims to develop an online repository of simple,
crude, yet easy-to-understand Python sample codes for dynamic complex
systems simulations, including iterative maps, cellular automata,
dynamical networks and agent-based models. You can run, read and
modify any of its codes to learn the basics of complex systems
simulation in Python.

The target audiences of PyCX are researchers and students who are
interested in developing their own complex systems simulation software
using a general-purpose programming language but do not have much
experience in computer programming.

The core philosophy of PyCX is therefore placed on the simplicity,
readability, generalizability and pedagogical values of simulation
codes. This is often achieved even at the cost of computational speed,
efficiency or maintainability. For example, PyCX does not use
object-oriented programming paradigms, it does use global variables
frequently, and so on. These choices were intentionally made based on
our experience in teaching complex systems modeling and simulation to
non-computer scientists.

For more information, please see the following open-access article:
Sayama, H. (2013) PyCX: A Python-based simulation code repository for
complex systems education. Complex Adaptive Systems Modeling 1:2.
http://www.casmodeling.com/content/1/1/2


2. What's new in version PyCX 0.3 / 0.31 / 0.32?

* Przemyslaw Szufel & Bogumil Kaminski at the Warsaw School of
  Economics made a substantial improvement to the "pycxsimulator.py"
  GUI module, implementing interactive control of model and
  visualization parameters. This improvement is fully backward
  compatible, so you can run old PyCX 0.2 simulator codes with this
  new GUI module.

* Several new sample simulation codes were added, including:

    Contributions by Przemyslaw Szufel & Bogumil Kaminski:
    - "abm-schelling.py" (Tom Schelling's segregation model)
    - "ca-rumor.py" (Spread of rumor)
    The above two codes show how to use the new interactive parameter
    setting feature.

    Other additions of dynamical network models:
    - "net-randomwalk.py" (Random walk on a network)
    - "net-voter.py" (Voter model of opinion formation on a network)
    - "net-epidemics-adaptive.py" (Epidemics on a network, with adaptive link cutting)
    - "misc-fileio-csv.py" (Example of how to read/write CSV files)

* Revision made to 0.31:
     - ttk is used as a graphics backend instead of Tix, so that Mac
       users can run the sample codes without installing Tix.

* Revision made to 0.32: 
    - The "pycxsimulator.py" GUI module was updated with several bug
      fixes by Toshi Tanizawa and Alex Hill to make its GUI and
      visualization more stable.
    - The file name of the Schelling's segregation model was changed
      to "abm-" to better reflect the nature of the model.
    - Sample codes used in Hiroki Sayama's Open SUNY textbook
      (http://tinyurl.com/imacsbook) are now included in the
      "textbook-sample-codes" subfolder.


3. How to use it?

(i) Install Python 2.7, NumPy, SciPy, matplotlib and NetworkX.
Installers are available from the following websites:
  http://python.org/  http://scipy.org/  http://matplotlib.org/  http://networkx.github.io/

Alternatively, you can use prepackaged Python suites, such as:
    - Anaconda (https://www.continuum.io/downloads)
    - Enthought Canopy (https://www.enthought.com/products/canopy/)

(ii) Choose a PyCX sample code of your interest.

(iii) Run it.

(iv) Read the code to learn how the simulation was implemented.

(v) Change the code as you like.


Note to Anaconda Spyder users:
* To run dynamic simulations, you should use a plain Python console
  (i.e., not in an IPython console). You can open a plain Python
  console from the "Consoles" menu.


Note to Enthought Canopy users:
* To run dynamic simulations, you may need to do the following:
  1. Go to "Edit" -> "Preferences" -> "Python" tab.
  2. Uncheck the "Use PyLab" check box, and click "OK."
  3. Choose "Run" -> "Restart kernel."
  4. Run your code. If it still doesn't work, re-check the "Use PyLab" check box, and try again.


Questions? Comments? Send them to sayama@binghamton.edu.
