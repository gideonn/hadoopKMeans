#!/usr/bin/env python

import sys
import json
import collections

clusterDict = collections.defaultdict(int)

for line in sys.stdin:
    line = json.loads(line)
    clusterID = line[0]
    dataPoints = line[1]
    #print("Cluster: {}".format(line[0]))
    #print("Datapoints: {}".format(line[1]))
    try:
        clusterDict[clusterID] = clusterDict[clusterID] + dataPoints
    except:
        clusterDict[clusterID] = [] + dataPoints

print(clusterDict)