#!/usr/bin/env python

import sys
import random
import numpy as np

global centroids
centroids = []

# filename = 'centroids.txt'

def loadCentroids(filename):
    #read centroids from the file
    with open(filename, 'r') as f:
        centroids.extend(float(center) for center in (f.read().split()))

    print("Centroids: {}".format(centroids))


def getDist(center, points):
    centerList = [center] * len(points)
    centerList = np.array(centerList)
    points = np.array(points)

    return np.linalg.norm(centerList - points)


def kmeansMapper(filename):

    loadCentroids(filename)
    points = []
    for line in sys.stdin:
        points = [float(point) for point in (line.split()[2:])]

        distance = float('inf')
        #Now for each centroid, find euclidean distance from all points
        for idx in range(len(centroids)):
            if distance > getDist(centroids[idx], points):
                distance = getDist(centroids[idx], points)
                kID = idx

        print([kID, points])

    return


# loadCentroids('centroids.txt')
kmeansMapper('centroids.txt')