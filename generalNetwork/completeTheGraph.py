# from __future__ import print_function
from globalVariables import *
import numpy as np
import sys
import random
import generateGraph as gg
import removeEdges as remE

def completeGraph(partialGr,theta0,hidden):
	# print(partialGr,np.sum(partialGr))
	# print(partialGr,np.sum(partialGr))
	samples = gg.MetropolisHasting(theta0,partialGr,hidden)
	return samples
# completeGraph(float(sys.argv[1]))