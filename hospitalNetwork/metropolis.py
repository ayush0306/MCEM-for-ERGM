import math
import copy	
import numpy as np
from globalVariables import *

def chooseNode(chooseFrom):
	tmp = random.choice(chooseFrom)
	return tmp

# def calkstar(adj,k):
# 	ans = 0
# 	for hub in hubs : 
# 		if nodes[hub].degree==k :
# 			ans+=1
# 	return ans

def ncr(n,r):
	npr = math.factorial(n)/math.factorial(n-r)
	ncr = npr/math.factorial(r)
	return ncr

def calkstar(adj,k):
	ans = 0
	for hub in hubs : 
		if nodes[hub].degree>=k :
			ans+=ncr(nodes[hub].degree,k)
	return ans

def calcStats(a,b,adj):
	stats = []
	for i in range(a,b+1):
		stats.append(calkstar(adj,i))
	return np.array(stats)

def toggle(adj,sp,oldh,newh):
	nodes[sp].remEdge(oldh)
	nodes[oldh].remEdge(sp)
	nodes[sp].addEdge(newh)
	nodes[newh].addEdge(sp)
	nodes[sp].hub = newh
	return adj

# def updateGr(kin,kout,theta,adj,curSt,chooseFrom):
# 	rndSpoke = chooseNode(chooseFrom)
# 	curHub = nodes[rndSpoke].hub
# 	newHub = random.choice(hubs)
# 	adj = toggle(adj,rndSpoke,curHub,newHub)
# 	newSt = calcStats(kin,kout,adj)
# 	if(np.dot(theta,(newSt-curSt))>0):
# 		ratio = 1
# 	else :
# 		ratio = math.exp(np.dot(theta,(newSt-curSt)))
# 	if random.random() <= ratio :
# 		return newSt,adj
# 	return curSt,toggle(adj,rndSpoke,newHub,curHub)

def updateGr(kin,kout,theta,adj,curSt,chooseFrom):
	curHubs = [i for i in range(nNodes+1)]
	for spoke in chooseFrom : 
		curHub = nodes[spoke].hub
		curHubs[spoke] = curHub
		newHub = random.choice(hubs)
		adj = toggle(adj,spoke,curHub,newHub)
	newSt = calcStats(kin,kout,adj)
	if(np.dot(theta,(newSt-curSt))>0):
		ratio = 1
	else :
		ratio = math.exp(np.dot(theta,(newSt-curSt)))
	if random.random() <= ratio :
		return newSt,adj
	for spoke in chooseFrom :
		oldHub = curHubs[spoke]
		curHub = nodes[spoke].hub
		adj = toggle(adj,spoke,curHub,oldHub)
	return curSt,adj

def MetropolisHasting(kin,kout,theta,adj,chooseFrom,burning=10000,nSamples=30,interval=50):
	# print(burning,nSamples,interval)
	curSt = calcStats(kin,kout,adj)
	# print(curSt)
	for i in range(burning):
		curSt,adj = updateGr(kin,kout,theta,adj,curSt,chooseFrom)
	samples = []
	for i in range(nSamples):
		for j in range(interval):
			curSt,adj = updateGr(kin,kout,theta,adj,curSt,chooseFrom)
		curSt,adj = updateGr(kin,kout,theta,adj,curSt,chooseFrom)
		# print(curSt,adj,calcStats(adj),sep='\n')
		samples.append([curSt,copy.deepcopy(adj)])
	return samples

# for spoke in spokes : 
# 	print(nodes[spoke].hub, end=" ")
# print()
# for hub in hubs : 
# 	print(hub,nodes[hub].degree)

