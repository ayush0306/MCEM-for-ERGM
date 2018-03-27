import random
import sys
import numpy as np
import dataParse as dparse
from globalVariables import *
import completeGraph as comGr
import generateScenarios as genSc

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
r=robjects.r
importr('ergm')
importr('network')


hubs,standalones,spokes = dparse.readData("mainData.csv")
# print(type(hubs),type(standalones),type(spokes))
nHubs,nSt,nSp = len(hubs),len(standalones),len(spokes)
nNodes = nHubs+nSt+nSp
adjList = [[0 for i in range(nNodes+1)] for j in range(nNodes+1)]
adjList,missing = data2graph(hubs,standalones,spokes,nNodes,adjList)
adjList = np.array(adjList)

print("Initial theta is : ",initialTh)
oldLogEst = 1e9

while True :
	graph,stats = comGr.completeGr(initialTh,adjList,missing,nHubs)
	print("Graph Completed")
	r.assign('n',nNodes)
	r('gr<-network.initialize(n,directed=F)')
	print("Graph Initialized")
	for i in range(1,nNodes+1):
		for j in range(1,nNodes+1):
			if(graph[i][j]==1):
				r.assign('i',i)
				r.assign('j',j)
				# r('m[i,j]=1')
				r('add.edge(gr,i,j)')
				r('add.edge(gr,j,i)')
	# r('plot(gr)')
	print("Graph in R made")
	# input("Please type enter...")
	r('typ = c(rep("Spoke",n))')
	for hub in range(1,nHubs+1) : 
		r.assign('i',hub)
		r('typ[i]="hub"')
	# r('print(typ)')
	r('set.vertex.attribute(gr,"type",typ)')
	print("Attributes assigned")
	print("Training....")
	r('model.01<-ergm(gr~edges)')
	newLogEst = r('logLik(model.01)')[0]
	print("Log Likelihood : ",newLogEst)
	newTh = r('model.01$coef')[0]
	print("New Theta is :",newTh)
	if(abs(newLogEst-oldLogEst)<epsilon):
		break
	oldLogEst = newLogEst
	initialTh = newTh

genSc.completeGr(initialTh,adjList,missing,nHubs,nSt,nSp)
