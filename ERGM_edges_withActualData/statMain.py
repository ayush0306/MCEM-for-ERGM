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

#Read File
hubs,standalones,spokes = dparse.readData(datafile)
# print(type(hubs),type(standalones),type(spokes))

nHubs,nSt,nSp = len(hubs),len(standalones),len(spokes)
nNodes = nHubs+nSt+nSp
adjList = [[0 for i in range(nNodes+1)] for j in range(nNodes+1)]
adjList,missing = data2graph(hubs,standalones,spokes,nNodes,adjList)
adjList = np.array(adjList)

print("Initial theta is : ",initialTh)
oldLogEst = 1e9

while True :
	'''Complete the missing graph using initialTh'''
	graph,stats = comGr.completeGr(initialTh,adjList,missing,nHubs)
	print("Graph Completed")
	r.assign('n',nNodes)
	r('gr<-network.initialize(n,directed=F)')
	# input("Please type enter...")

	print("Converting Stats in R form")
	# stats = list(stats)
	statList = [int(stats)]
	resTmp = robjects.IntVector(statList)
	r.assign('rSt',resTmp)

	print("Training....")
	'''Fit the ergm model to the statistics of the obtained graph from completing the missing edges'''
	r('model.01<-ergm(gr~edges,target.stats=rSt, eval.loglik=TRUE)')
	newLogEst = r('logLik(model.01)')[0]
	newTh = r('model.01$coef')[0]
	print("Log Likelihood : ",newLogEst)
	print("New Theta is :",newTh)
	'''If the Log likelihood doesn't increase by much, stop the MCEM algorithm and return theta as the desired value.'''
	if(abs(newLogEst-oldLogEst)<epsilon):
		break
	oldLogEst = newLogEst
	initialTh = newTh

'''Generate Scenarios'''
genSc.generate(initialTh,adjList,missing,nHubs,nSt,nSp)