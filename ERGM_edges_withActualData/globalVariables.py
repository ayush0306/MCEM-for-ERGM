import random
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
r=robjects.r
importr('ergm')
importr('network')

nodes = []  #List of all instances of Class Node - includes all hubs, standalones and spokes. 

'''Parameters for MCMC sampling'''
burningVal = 1000  
sampleCount  = 30
intervalBwSamples = 50

nScenarios = 50 #No. of scenarios to be generated at the end
epsilon = 1 #Error margin in Log Likelihood Estimate. Convergence criterion for MCEM. 
initialTh = 3.0 #The initial theta to begin MCEM.
datafile = "mainData.csv" #Name of the input data file
outfile = "scenarios" #Name of the output file. Contains the required scenarios. 

'''Given an adjacency matrix, this function plots the graph in R. Useful for visualization purposes'''
def plotGraph(graph,grname):
	r.assign('n',nNodes)
	r('m<-matrix(0,n,n)')
	for i in range(1,nNodes+1):
		for j in range(1,nNodes+1):
			if(graph[i-1][j-1]==1):
				r.assign('i',i)
				r.assign('j',j)
				r('m[i,j]=1')
	r('gr<-network(m)')
	r.assign('grname',str("./graphPlots/"+grname))
	r('png(filename=grname)')
	r('plot(gr, displaylabels = TRUE)')
	r('dev.off()')
	# input("Please press enter...")
	return

'''Class for each Node. self.ind is the index in the nodes[] list declared above.'''
class Node():
		def __init__(self,ind,name,kind,hub,degree=0):
			self.ind = ind
			self.name = name
			self.kind = kind
			self.hub = hub
			self.degree = degree

		def addEdge(self,ver,adj):
			self.degree += 1
			adj[self.ind][ver]=1
			return adj
		
		def remEdge(self,ver,adj):
			self.degree -= 1
			adj[self.ind][ver]=0
			return adj

'''This uses the filtered data to construct a graph (adjacency matrix) and a node object for each node. '''
def data2graph(h,st,sp,nNodes,adj):
	nHubs,nSpokes = len(h),len(sp)
	hub_nameToInd = {}
	missing = []
	nodes.append(Node(0,"empty","empty",0,0))
	ind = 1
	'''For Hubs'''
	for i in range(len(h)):
		hname = h.iloc[i]["provider_name"]
		nodes.append(Node(ind,hname,"hub",ind,0))
		hub_nameToInd[hname] = ind 
		ind+=1
	'''For standalones'''
	for i in range(len(st)) :
		stName = st.iloc[i]["provider_name"] 
		nodes.append(Node(ind,stName,"standalones",ind,0))
		ind+=1
	count,tmp = 0,0
	'''For spokes. Here the ref_provider_name is used to construct the edges.'''
	for i in range(len(sp)) :
		spName = sp.iloc[i]["provider_name"]
		if(str(sp.iloc[i]["ref_provider_name"])=="nan"):
			count+=1
			randHub = random.randint(1,nHubs) #assign random hub initially to spokes for which the ref_provider_name is not present.
			nodes.append(Node(ind,spName,"spokes",randHub,0))
			missing.append(ind)
			adj = nodes[ind].addEdge(randHub,adj)
			adj = nodes[randHub].addEdge(ind,adj)
		else : 
			tmp+=1
			refHub = hub_nameToInd[sp.iloc[i]["ref_provider_name"]]
			nodes.append(Node(ind,spName,"spokes",refHub,0))
			adj = nodes[ind].addEdge(refHub,adj)
			adj = nodes[refHub].addEdge(ind,adj)
		ind+=1
	print(count,tmp)
	return adj,missing

