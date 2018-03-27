from __future__ import print_function
import pandas as pd


def readData(filename):
	#Read the file into a panda data fram
	inp = pd.read_csv(filename)

	#Extract hubs, standalones and spokes
	hubs = inp[inp.ABC=="A"]["provider_name"]
	standalones = inp[inp.ABC=="B"]
	spokes = inp[inp.ABC=="C"]["provider_name"]
	print("Hubs : ",len(hubs)," Standalones : ",len(standalones)," Spokes : ",len(spokes))

	# For all the spokes for which the reference provider name is known, extract all such reference providers (essentially the hubs that are being referred.)
	spKaHub = inp[(inp.ABC=="C") & ~(inp.ref_provider_name.isnull())]["ref_provider_name"]
	# Extract all the spokes for which the reference provider name is not known (missing data)
	SpMissing_Hub = inp[(inp.ABC=="C") & (inp.ref_provider_name.isnull())]["provider_name"]
	#Extract all spokes for which the reference provider name is known.
	SpExisting_Hub = inp[(inp.ABC=="C") & ~(inp.ref_provider_name.isnull())]["provider_name"]
	print("No. of spokes for which hubs are not known : ",len(SpMissing_Hub)," known : ",len(SpExisting_Hub))

	# Hubs that are referred to by other spokes (spKaHub) but for which we have no information about (not present in hubs)
	refNotPresent = spKaHub[~spKaHub.isin(hubs.get_values())]
	# Hubs that are both referred by other spokes and for which information is present. 
	refAndPresent = spKaHub[spKaHub.isin(hubs.get_values())]

	print("Out of the the spokes with known hubs, no. of spokes that refer to a hospital that we have no info are : ",len(refNotPresent)," that we have info : ",len(refAndPresent))

	PresentNotRef = hubs[~hubs.isin(spKaHub.get_values())]
	print("No. of hubs that we have info but are not referred : ",len(PresentNotRef))

	PresentAndRef = hubs[hubs.isin(spKaHub.get_values())]
	print("No. of distict hubs that we have info and about and are referred : ",len(PresentAndRef))


	#Making a toy network. Removing all the hubs that are not referred and all the spokes that refer to hubs with no info. 
	
	# Choosing only those spokes for which ref provider name is either missing or is one for which information is present.
	spokes_new = inp[(inp.ABC=="C") & ((inp.ref_provider_name.isin(hubs.get_values())) | (inp.ref_provider_name.isnull()))]
	print("No. of spokes with none referring to unknown hubs are : ",len(spokes_new))


	spKaHub_new = spokes_new[~(spokes_new.ref_provider_name.isnull())]["ref_provider_name"]
	
	# Similarly, choosing hubs that have been referred to by atleast one spoke in spokes_new. 
	hubs_new = inp[(inp.ABC=="A") & (inp.provider_name.isin(spKaHub_new.get_values()))]
	print("No. of hubs that are referred by atleast one spoke are : ",len(hubs_new))

	return hubs_new,standalones,spokes_new


# hubs,standalones,spokes = readData("mainData.csv")
# print(len(hubs),len(standalones),len(spokes))
