
# Running k-means on a Map Reduce framework

##### Make sure that the data file are present in the right places, hadoop namenode and datanodes are up.

##### Assuming the HDFS contains a directory output where the output will be written. That can easily be changed by changing the path in runKMeans.sh file.

## Creating k-random centroids
* Run setup.py file, enter the name of the input file and value of k.
* This will create a file called "centroids.txt" that will hold k random values from the input file.

## Running map reduce
* Run the bash script runKMeans.sh, enter the name of the input file as input.
* This script does multiple things.
* Copy the input file to HDFS
* Call the map reduce streaming API with correct parameters
* Loop till convergence

## Analyizing and Plotting
* Run the results.py file, entering the name of the input file when prompted.
* The script will print the Rand co-efficient and Jaccard co-efficient alongwith showing the plot. 

