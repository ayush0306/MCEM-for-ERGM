"""USING ERGM TO PREDICT THE MISSING EDGES IN A NETWORK AND GENERATE SCENARIOS"""

1. Contents : 

- The directory contains 8 files, namely, 

a. README.txt : This file that explains about the program. 
b. globalVariables.py : This file is where the different parameters are defined and is used across other files. It also contains the class structure of the nodes in the graph and other methods. Please refer to the file to know the exact functionality of each method. 
c. mainData.csv : This contains our actual data in the form of a csv file. 
d. dataParse.py : This contains the method to parse ur data into the required form for further use. 
e. completeGraph.py : It contains the method to fill the missing edges into a graph (passed as an adjacency matrix).
f. metropolis.py : Contains the methods necessary to carry out the MCMC sampling. 
g. main.py : this is the master file which needs to be called to execute our program.
h. statMain.py : it is similar to the main.py file, but it differs in the way the ergm is used to fit the graph. In the former, the completed graph is remade in R and the ergm fits its model on it, while in the latter, we pass the target statistics as an argument. The latter works faster. 

2. How to setup the environment and run the code.

- Make sure you have Python3 installed in your system. 
- Libraries Needed : pandas, numpy, rpy2. random and sys libraries should be pre installed (if not, install them too.) 
- Setup up a working directory with a name of your choice. 
- Download all the files assosciated with this directory to your own. Preferrably, don't change the name of the files as filenames are used to refer each other. If you do change the filename, make sure to replace all the instances of the filename in any code file. 
- In your working directory, inititiate the python3 shell and execute the "main.py" or "statMain.py" file to run the code. 

2. Parameters and variables to the program.

- all the parameters and their explaination are mentioned in the file "globalVariables.py".

3. Input and Output to the Program 

- Input : mainData.csv - this is the collected data in a csv format. Make sure to keep the file in the same directory as the other codes. If you choose to change the name of the file, make sure to change the name in globalVariables.py

- Output : scenarios - The output file contains the information for the desired no. of scenarios (defined in globalVariables.py with variable nScenarios). For each sccenario, it contains, nHubs (no. of hubs) lines. Each line starts with the name of a hub followed by a colon (:), and the comma seperated list of all the spokes that it is connected to. 