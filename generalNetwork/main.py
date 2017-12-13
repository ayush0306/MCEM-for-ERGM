# from __future__ import print_function

import random
import sys
import numpy as np
from globalVariables import *
import generateGraph as gg 
import removeEdges as remE
import completeTheGraph as comp
import newtonRaphson as newRap

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
r= robjects.r
importr('ergm')
importr('network')


theta = float(sys.argv[1])
partialGr = remE.partialGraph(theta)
hidden = []
for i in range(nNodes):
	for j in range(i+1,nNodes):
		if partialGr[i][j]==-1:
			hidden.append((i,j))
			partialGr[i][j]=0
			partialGr[j][i]=0
theta0 = 5.0
while True : 
	print("Theta0 : ",theta0)
	r('grp <- network.initialize(12, directed=F)')
	# r('plot(grp)')
	# exit(0)
	completed = comp.completeGraph(partialGr,theta0,hidden)

	stats = 0
	for i in range(len(completed)):
		stats+=completed[i][0]
	stats = stats/len(completed)
	# stats = robjects.FloatVector(stats)
	# print(stats)
	# r('summary(stats)')
	# exit(0)
	r.assign('rStat',stats)
	r('rSt <- c(rStat)')
	r('model.01<-ergm(grp~edges,target.stats=rSt)')
	r('model.01$coef')
	# exit(0)
	# r =robjects.r
	# retVal = r.source("RCode.R")
	# print(retVal)
	newTheta = r('model.01$coef')[0]
	if(abs(newTheta - theta0))<0.01	: 
		break 
	theta0 = newTheta