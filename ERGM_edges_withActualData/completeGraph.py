from __future__ import print_function
from metropolis import *

def completeGr(theta,adj,chooseFrom,nHubs):
	samples = MetropolisHasting(theta,adj,chooseFrom,nHubs)
	avgstat = 0
	for sample in samples :
		avgstat += sample[0]
	avgstat /= len(samples)
	# print(avgstat)
	return samples[0][1],avgstat
	# return samples[-1][0]