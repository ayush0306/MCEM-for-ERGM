import random
import numpy as np
from metropolis import *
from globalVariables import *

for spoke in spokes : 
	hub = random.choice(hubs)
	# print(spoke,hub)
	nodes[spoke].hub = hub
	nodes[spoke].addEdge(hub)
	nodes[hub].addEdge(spoke)

adjList = np.array(adjList)
print(np.sum(adjList))
# theta = []
# for i in range(kin,kout+1):
# 	print("Enter the coefficient for the ",i,"th input",sep="",end=":")
# 	theta.append(float(input()))
# print(theta)
# exit(0)
theta = [-3.1,-1,-0.6,-0.2,-1,-0.5,-3.0,-4.0]
adjList = MetropolisHasting(kin,kout,theta,adjList,spokes)[0][1]
for spoke in spokes :
	print(spoke,nodes[spoke].hub)
for hub in hubs :
	print(hub,nodes[hub].degree)