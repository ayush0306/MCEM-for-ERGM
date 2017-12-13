from generateGraph import *
from metropolis import *
from globalVariables import *

def completeGr(kin,kout,theta,adj,chooseFrom):
	samples = MetropolisHasting(kin,kout,theta,adj,chooseFrom)
	avgstat = np.zeros(kout-kin+1)
	for sample in samples :
		avgstat += sample[0]
	avgstat /= len(samples)
	print(avgstat)
	return samples[0][1],avgstat
	# return samples[-1][0]