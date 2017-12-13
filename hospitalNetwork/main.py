import random
import sys
import numpy as np
from globalVariables import *
from generateGraph import *
from completeGraph import *

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
r=robjects.r
importr('ergm')
importr('network')

initialTh = []
for i in range(kin,kout+1):
	initialTh.append(random.randint(-2,2))
intitialTh = np.array(initialTh)
print(initialTh)

while True :
	graph,stats = completeGr(kin,kout,initialTh,adjList,missing)
	# for spoke in spokes :
	# 	print(spoke,nodes[spoke].hub)
	# for hub in hubs :
	# 	print(hub,nodes[hub].degree)
	stats = stats+np.ones(len(stats))
	stats = list(stats)
	resTmp = robjects.IntVector(stats)
	print(resTmp)
	r.assign('rSt',resTmp)
	r('print(rSt)')
	# r('print(dim(rSt))')
	r('gr<-network.initialize(36,directed=F)')
	r.assign('kin',kin)
	r.assign('kout',kout)
	r('model.01<-ergm(gr~kstar(kin:kout),target.stats=rSt)')
	exit(0)
# intitialTh = [2,4] #No. of edges and k-star
