# from __future__ import print_function
import numpy as np

def f(theta0,theta,s1,s2):
	print("For theta = ",theta)
	thetaTmp = theta-theta0
	if(thetaTmp>0):
		norm = thetaTmp*np.min(s2)
	else:
		norm = thetaTmp*np.max(s2)
	print("Norm is : ",norm)
	# norm = 0
	tmp = np.exp(thetaTmp*s2-norm)
	# print("Tmp is : ",tmp)
	num = np.dot(s2,tmp)
	den = np.sum(tmp)
	print(num,float(den))
	return (float(np.sum(s1))/len(s1))-(float(num)/float(den))

def df(theta0,theta,s1,s2):
	h = float(theta)/10
	t1 = f(theta0,theta+h,s1,s2)
	t2 = f(theta0,theta,s1,s2)
	# print(t1,t2,h)
	tmp = (t1-t2)/float(h)
	print("df is ",tmp)
	return tmp

def updateTheta(theta0,theta,s1,s2):
	return theta - (f(theta0,theta,s1,s2)/df(theta0,theta,s1,s2))

def newtonRap(theta0,s1,s2):
	s1,s2 = np.array(s1),np.array(s2)
	epsilon = 0.1
	theta = float(2)
	nIters = 5
	while nIters>0 : 
		print("Theta is ",theta,"and f Theta is",f(theta0,theta,s1,s2))
		newTh = updateTheta(theta0,theta,s1,s2)
		print("Updated Theta is ",newTh)
		# exit(0)
		change = abs(f(theta0,theta,s1,s2)-f(theta0,newTh,s1,s2))
		if(change < epsilon):
			break 
		theta = newTh
		nIters-=1
	return theta

