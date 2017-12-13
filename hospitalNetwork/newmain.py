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
	# stats = stats+np.ones(len(stats))
	# stats = list(stats)
	# resTmp = robjects.IntVector(stats)
	# print(resTmp)
	# r.assign('rSt',resTmp)
	# r('print(rSt)')
	# r('print(dim(rSt))')
	r.assign('n',nNodes)
	r('m<-matrix(0,n,n)')
	for i in range(1,nNodes+1):
		for j in range(1,nNodes+1):
			if(graph[i][j]==1):
				r.assign('i',i)
				r.assign('j',j)
				r('m[i,j]=1')
	r('gr<-network(m)')
	r('plot(gr)')
	input("Please type enter...")
	r('typ = c(rep("Spoke",n))')
	for hub in hubs : 
		r.assign('i',hub)
		r('typ[i]="hub"')
	r('print(typ)')
	r('set.vertex.attribute(gr,"type",typ)')
	r('plot(gr, displaylabels = TRUE)')
	input("Please type enter...")
	# exit(0)
	print(len(completeGraph))
	r.assign('kin',kin)
	r.assign('kout',kout)
	# r('model.01<-ergm(gr~kstar(kin:kout),target.stats=rSt)')
	exit(0)
# intitialTh = [2,4] #No. of edges and k-star
