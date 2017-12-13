# from __future__ import print_function
import sys
import random
import numpy as np
import generateGraph as gg
from globalVariables import *


def partialGraph(theta):
	chooseFrom = []
	for i in range(nNodes):
		for j in range(i+1,nNodes):
			chooseFrom.append((i,j))
	samples = gg.generateGr(theta)
	sampleIndex = random.randint(0,len(samples)-1)
	sample = np.array(samples[sampleIndex][1])
	partialSample = sample.copy()

	# all_zeros = not (sample-np.transpose(sample)).any()
	# print(all_zeros)

	# print("No. of 1s : ",np.sum(sample))
	toRemove = int(np.sum(sample)/8)
	# toRemove = 0
	# print("No. of -1s : ",toRemove*2)

	count = 0 
	while(count < toRemove):
		a,b = gg.chooseNode(chooseFrom)
		if(partialSample[a][b]==1):
			partialSample[a][b]=-1
			partialSample[b][a]=-1
			count += 1

	# f = open("partial",'w')
	# for i in range(nNodes):
	# 	for j in range(nNodes):
	# 		f.write(str(partialSample[i][j])+" ")
	# 	f.write("\n")
	# f.close()
	
	return partialSample

partialGraph(float(sys.argv[1]))

