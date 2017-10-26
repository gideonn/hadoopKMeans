#!/usr/bin/env python

import sys
import json
import collections
import math

clusterDict = collections.defaultdict(int)

def getCentroids(filename):
    with open(filename) as f:
        centroids = f.readline().split()

    return centroids

for line in sys.stdin:
    line = json.loads(line)
    clusterID = line[0]
    dataPoints = line[1]
    #print("Cluster: {}".format(line[0]))
    #print("Datapoints: {}".format(line[1]))
    try:
        clusterDict[clusterID] = clusterDict[clusterID] + dataPoints
    except:
        #handle the case where clusterDict[clusterID] gives 0
        clusterDict[clusterID] = [] + dataPoints


with open('clusterData.txt', 'a') as f:
    f.write("---- \n")
    for key,val in clusterDict.items():
        data = str(key) + ' : ' + ' '.join(str(v) for v in val)
        f.write(data)

#read centroids.txt to get old centroid values
oldCentroids = getCentroids('centroids.txt')
newCentroids = oldCentroids[:]

#for the clusters having datapoints, get the new centroids and update the old centroid with the new one
for idx in range(len(oldCentroids)):
    if clusterDict.get(idx):
        newCenter = math.floor(sum(clusterDict[idx])/len(clusterDict[idx]),5)
        newCentroids[idx] = newCenter

print("Old centroids: {}".format(oldCentroids))
print("New centroids: {}".format(newCentroids))

with open('centroids.txt','w') as f:
    f.write(' '.join(str(point) for point in newCentroids))

#stop the iteration if new centroid = old centroid for centroids with datapoints
if oldCentroids == newCentroids:
    print("Stopping iteration!!!")

# print(clusterDict)