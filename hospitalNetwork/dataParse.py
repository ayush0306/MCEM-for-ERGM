from __future__ import print_function

hubs = []
spokes = []

f = open("new_data.csv",'r')
lines = f.readlines()

columns = lines[0].split(",")
KeyToInd = {}
for i,col in enumerate(columns) :
	KeyToInd[col]=i
# print(KeyToInd)

count = 0
for line in lines[1:] :
	entries = line.split(",")
	sp = entries[KeyToInd['provider_name']]
	hub = entries[KeyToInd['ref_provider_name']]
	if sp and not hub : 
		count+=1
	if sp and (sp not in spokes):
		spokes.append(sp)
	if hub and (hub not in hubs):
		hubs.append(hub)
	# print(line)
print(len(spokes),len(hubs))
missingHub = []
for hub in hubs :
	if hub not in spokes : 
		missingHub.append(hub)
print(len(missingHub))
print(count)