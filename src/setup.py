#!/usr/bin/env python

from random import random

def createCentroidsFile(k, inputFile):

    centroids = [line.split()[2:] for line in open(inputFile) if random() >= .5][:k]

    with open('centroids.txt', 'w') as f:
        for center in centroids:
            f.write(' '.join(str(point) for point in center))
            f.write("\n")

def cleanFiles():
    #delete result cluster data points
    pass

if __name__ == '__main__':
    inputFile = input("Enter the name of the input file: ")
    k = int(input("Enter the number of clusters desired: "))
    createCentroidsFile(k, inputFile)