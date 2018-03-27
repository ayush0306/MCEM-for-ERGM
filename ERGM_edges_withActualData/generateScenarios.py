from __future__ import print_function
from metropolis import *

def write2file(adj,nh,nst,nsp):
	f = open(outfile,'a+')
	for i in range(1,nh+1):
		f.write('"'+str(nodes[i].name)+'"'+" : ")
		for j in range(1+nh+nst,1+nh+nst+nsp):
			if(int(adj[i][j]==1)):
				# f.write(str(j)+" ")
				f.write('"'+str(nodes[j].name)+'"'+",")
		f.write("\n")
	# f.write("\n")
	f.close()


def generate(theta,adj,chooseFrom,nHubs,nStandalones,nSpokes):
	samples = MetropolisHasting(theta,adj,chooseFrom,nHubs,burningVal,nScenarios)
	f = open("scenarios",'w+')
	f.close()
	for sample in samples : 
		# print(len(sample[1]))
		# print(nHubs,nStandalones,nSpokes,nHubs+nStandalones+nSpokes)
		write2file(sample[1],nHubs,nStandalones,nSpokes)
	# return samples[-1][0]