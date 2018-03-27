import math
import copy	
import numpy as np
from globalVariables import *

def chooseNode(chooseFrom):
	tmp = random.choice(chooseFrom)
	return tmp

def calEdges(adj):
	return np.sum(adj)/2

def calcStats(adj):
	stats = calEdges(adj)
	return stats

def toggle(adj,sp,oldh,newh):
	adj = nodes[sp].remEdge(oldh,adj)
	adj = nodes[oldh].remEdge(sp,adj)
	adj = nodes[sp].addEdge(newh,adj)
	adj = nodes[newh].addEdge(sp,adj)
	nodes[sp].hub = newh
	return adj

'''THe function chooses a spoke at random, assign it to another random hub. 
We update the graph based on the ratio of the probability of observing the new and the previous graph. '''

def updateGr(theta,adj,curSt,chooseFrom,nHubs):
	nNodes = len(adj)
	spoke = chooseNode(chooseFrom)  #Choose a spoke with missing edge
	curHub = nodes[spoke].hub
	newHub = random.randint(1,nHubs+1)  #Assign it to a random hub
	adj = toggle(adj,spoke,curHub,newHub)

	# Use the Metropolis Rule to update the graph
	newSt = calcStats(adj)   
	if(theta*(newSt-curSt))>0:
		ratio = 1
	else :
		ratio = math.exp(theta*(newSt-curSt))
	if random.random() <= ratio :
		return newSt,adj
	adj = toggle(adj,spoke,newHub,curHub)
	return curSt,adj

def MetropolisHasting(theta,adj,chooseFrom,nHubs,burning=burningVal,nSamples=sampleCount,interval=intervalBwSamples):
	# print(burning,nSamples,interval)
	# print(nodes[0].name,nodes[0].hub)
	# exit(0)
	curSt = calcStats(adj)
	# print(curSt)
	for i in range(burning):
		# print(i,end=" ")
		curSt,adj = updateGr(theta,adj,curSt,chooseFrom,nHubs)
	samples = []
	for i in range(nSamples):
		for j in range(interval):
			curSt,adj = updateGr(theta,adj,curSt,chooseFrom,nHubs)
		curSt,adj = updateGr(theta,adj,curSt,chooseFrom,nHubs)
		# print(curSt,adj,calcStats(adj),sep='\n')
		samples.append([curSt,copy.deepcopy(adj)])
	return samples

# for spoke in spokes : 
# 	print(nodes[spoke].hub, end=" ")
# print()
# for hub in hubs : 
# 	print(hub,nodes[hub].degree)

