import random

nNodes = 36
nHubs = 6
adjList = [[0 for i in range(nNodes+1)] for j in range(nNodes+1)]
kin = 2
kout = 8
allNodes = [i for i in range(1,nNodes+1)]
hubs = [3,2,9,15,7,19]
spokes = []

class Node():
		def __init__(self,ind,kind,hub,degree=0):
			self.ind = ind 
			self.kind = kind
			self.hub = hub
			self.degree = degree

		def addEdge(self,ver):
			self.degree += 1
			adjList[self.ind][ver]=1
		
		def remEdge(self,ver):
			self.degree -= 1
			adjList[self.ind][ver]=0

for node in allNodes :
	if node not in hubs :
		spokes.append(node)

nodes = [0 for i in range(nNodes+1)]
for i in hubs : 
	nodes[i] = Node(i,"hub",i,0)
for i in spokes :
	nodes[i] = Node(i,"spoke",i,0)

random.shuffle(spokes)
known = int(len(spokes)*0.75)
missing = spokes[known:]