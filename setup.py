
import random

def createCentroidsFile(k, inputFile):

    with open(inputFile) as f:
        data = f.readline().split()

    random.shuffle(data)
    centroids = data[:k]

    with open('centroids1.txt', 'w') as f:
        f.write(' '.join(centroids))

    print("Created centroids.txt with centroids as :{}".format(' '.join(centroids)))



if __name__ == '__main__':
    inputFile = input("Enter the name of the input file: ")
    k = int(input("Enter the number of clusters desired: "))
    createCentroidsFile(k, inputFile)