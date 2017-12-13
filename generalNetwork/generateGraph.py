	# from __future__ import print_function
import matplotlib.pyplot as plt
import math
import random
import operator
import numpy as np
import sys
import copy
from globalVariables import *
random.seed()

def chooseNode(chooseFrom):
	# randInd = int(random.random()*(len(chooseFrom)-1))
	# tmp = chooseFrom[randInd]
	# print(len(chooseFrom))
	tmp = random.choice(chooseFrom)
	return tmp[0],tmp[1]

def calcStats(adj):
	return np.sum(adj)/2

def toggle(adj,a,b):
	adj[a][b] = 1-adj[a][b]
	adj[b][a] = 1-adj[b][a]
	return adj

def updateGr(theta,adj,curSt,chooseFrom):
	nNodes = adj.shape[0]
	a,b = chooseNode(chooseFrom)
	adj = toggle(adj,a,b)
	newSt = calcStats(adj)
	ratio = math.exp(theta*(newSt-curSt))
	if random.random() <= ratio :
		return newSt,adj
	return curSt,toggle(adj,a,b)


def MetropolisHasting(theta,adj,chooseFrom,burning=10000,nSamples=30,interval=50):
	# print(burning,nSamples,interval)
	curSt = calcStats(adj)
	for i in range(burning):
		curSt,adj = updateGr(theta,adj,curSt,chooseFrom)
	samples = []
	for i in range(nSamples):
		curSt,adj = updateGr(theta,adj,curSt,chooseFrom)
		# print(curSt,adj,calcStats(adj),sep='\n')
		samples.append([curSt,copy.deepcopy(adj)])
		for j in range(interval):
			curSt,adj = updateGr(theta,adj,curSt,chooseFrom)
	return samples


def generateGr(theta,burning=10000,nSamples=30,interval=50):
	chooseFrom = []
	for i in range(nNodes):
		for j in range(i+1,nNodes):
			chooseFrom.append((i,j))
	adj = np.zeros((nNodes,nNodes))
	samples = MetropolisHasting(theta,adj,chooseFrom,burning,nSamples,interval)
	return samples

# samples = generateGr(float(sys.argv[1]))
# print(samples[0][0])
# print(samples[0][1])