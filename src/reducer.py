#!/usr/bin/env python

import sys
import json
import collections
import math

clusterDict = collections.defaultdict(int)
geneIDDict = collections.defaultdict(int)


for line in sys.stdin:
    # print("Line:" + line)
    line = json.loads(line)

    clusterID = line[0]
    geneID = line[1][0]
    dataPoints = line[1][1:]

    # print("ClusterID: {} \n geneID: {} \n dataPoints: {}".format(clusterID,geneID,dataPoints))

    try:
        clusterDict[clusterID] = clusterDict[clusterID] + [dataPoints]
    except:
        #handle the case where clusterDict[clusterID] gives 0
        clusterDict[clusterID] = [] + [dataPoints]

    try:
        geneIDDict[clusterID] = geneIDDict[clusterID] + [geneID]
    except:
        # handle the case where clusterDict[clusterID] gives 0
        geneIDDict[clusterID] = [] + [geneID]

    # print(clusterDict)

#for each clusterID, iterate the list, for each first item in list avg and get the new centroid list for that clusterID
newCentroidVals = []
oldCentroidVals = []

for key, val in clusterDict.items():
    #key is clusterID, val is list of lists. Do a column by column addition
    singleCentroidVals = []
    for centroidVal in [round(sum(idx)/len(val),7) for idx in zip(*val)]:
        singleCentroidVals.append(centroidVal)

    newCentroidVals.append(singleCentroidVals)

#check if old centroid = new centroid
#load old centroids from file centroids.txt
with open('centroids.txt', 'r') as f:
    for line in f:
        oldCentroidVals.append([float(data) for data in line.split()])


if oldCentroidVals == newCentroidVals:
    with open('clusterResults.txt', 'w') as f:
        f.write(json.dumps(geneIDDict))

    with open('dataPointsResults.txt', 'w') as f:
        f.write(json.dumps(clusterDict))

    with open('stopIteration', 'w') as f:
        f.write(" ")

    #exit the reducer
    exit(0)

#if different from oldCentroids, update the new centroid in centroids.txt

with open('centroids.txt', 'w') as f:
    for idx in range(len(newCentroidVals)):
        f.writelines(' '.join(str(val) for val in newCentroidVals[idx]))
        f.write("\n")
