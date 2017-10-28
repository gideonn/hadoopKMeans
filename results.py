import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler

def loadDataSet(filePath):
    data_set = []
    with open(filePath) as file:
        for line in file:
            items = line.split('\t')
            res_line = [float(val) for i, val in enumerate(items[:-1])]
            last_item = float(items[-1].replace('\n', ''))
            res_line.append(last_item)
            data_set.append((res_line))
    # print(data_set)
    return data_set

class Gene(object):
    id = 0
    cluster = 0
    point = []

    def __init__(self, id, cluster, point):
        self.id = id
        self.cluster = cluster
        self.point = point

def make_gene(point):
    gene = Gene(int(point[0]),int(point[1]), point[2:])
    return gene

def getPairs(data_points):
    pairs = []
    for i in range(len(data_points)):
        for j in range(i + 1, len(data_points)):
            pairs.append([data_points[i], data_points[j]])
            pairs.append([data_points[j], data_points[i]])

    return pairs


#Create ground truth matrix
def createGroundTruthMatrix(data_set):
    Matrix = [[0 for x in range(len(data_set))] for y in range(len(data_set))]
    dict = {}
    # print(Matrix)
    # print(data_set)
    for j in range(0, len(data_set)):
        gene = make_gene(data_set[j])
        key = gene.cluster
        if key in dict:
            dict[key].append(gene)
        else:
            dict[key] = [gene]

    for key in dict.keys():
        genes = dict[key]
        ids = [gene.id for gene in genes]
        # print(key)
        # print(ids)
        pairs = getPairs(ids)
        for p in pairs:
            Matrix[p[0]-1][p[1]-1] = 1
    return Matrix


#Create cluster matrix
def createClusterMatrix(data_set_length):

    dict = json.load(open('clusterResults.txt'))

    Matrix = [[0 for x in range(data_set_length)] for y in range(data_set_length)]
    for key in dict.keys():
        genes = dict[key]
        ids = [geneID[0] for geneID in genes]
        # print(ids)
        pairs = getPairs(ids)
        # print(pairs)
        for p in pairs:
            Matrix[p[0]-1][p[1]-1] = 1
    return Matrix


# returns incidence matrix
def createIncidenceMatrix(cluster_matrix, ground_truth_matrix):
    Matrix = [[0 for x in range(2)] for y in range(2)]
    for i in range(len(cluster_matrix)):
        for j in range(len(cluster_matrix)):
            if cluster_matrix[i][j] == ground_truth_matrix[i][j]:
                if cluster_matrix[i][j] == 1:
                    Matrix[0][0] += 1 #same cluster,same cluster
                else:
                    Matrix[1][1] += 1 #different cluster, different cluster
            else:
                if cluster_matrix[i][j] == 1:
                    Matrix[0][1] += 1 #different cluster, same cluster
                else:
                    Matrix[1][0] += 1 #same cluster, different cluster
    #print Matrix
    return Matrix

# returns rand coefficient
def calculateRandCoefficient(incidence_matrix):

    num = float(incidence_matrix[0][0] + incidence_matrix[1][1])
    den = float(incidence_matrix[0][0] + incidence_matrix[1][1] + incidence_matrix[0][1] + incidence_matrix[1][0])
    randCoefficient = num/den

    return randCoefficient

#returns Jaccard coefficient
def calculateJaccardCoefficient(incidence_matrix):

    num = float(incidence_matrix[0][0])
    den = float(incidence_matrix[0][0] + incidence_matrix[0][1] + incidence_matrix[1][0])
    jaccardCoefficient = num/den

    return jaccardCoefficient


# perform PCA
def PCA(dic):
    c = []
    data = []
    for key in dic:
        for i in range(len(dic[key])):
            c.append(key)
            data.append(dic[key][i])
    finalData = np.array(data)
    labels = np.array(c)
    # print(finalData)
    # print(labels)
    pca = decomposition.PCA(n_components=2)
    finalData = np.mat(pca.fit_transform(finalData))

    return finalData, labels

# plot graph
def plotGraph(filename, finalData,labels):
    #create dataframe and group based on labels
    df = pd.DataFrame(dict(x=np.asarray(finalData.T[0])[0], y=np.asarray(finalData.T[1])[0], label=labels))
    groups = df.groupby('label')
    fig, ax = plt.subplots()
    ax.margins(0.05)

    #plot all datapoints
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=5, label=name)

    ax.legend()
    ax.set_title('Algorithm: KMeans\n Input file: ' + filename)
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')

    plt.savefig(filename + ".png", dpi=300)
    plt.show()


if __name__ == '__main__':

    inputFile = input("Enter the input file name which was used for processing: ")
    data_set = loadDataSet(inputFile);

    ground_truth_matrix = createGroundTruthMatrix(data_set)
    # print(len(ground_truth_matrix))

    cluster_matrix = createClusterMatrix(len(data_set))
    # print(cluster_matrix)

    # create incidence matrix
    incidence_matrix = createIncidenceMatrix(cluster_matrix, ground_truth_matrix)

    # calculate rand coefficient
    randCoefficient = calculateRandCoefficient(incidence_matrix)

    # calculate jaccard coefficient
    jaccardCoefficient = calculateJaccardCoefficient(incidence_matrix)

    print("Rand Co-efficient: ",randCoefficient)
    print("Jaccard Co-efficient: ", jaccardCoefficient)


    #Plotting the clusters using PCA
    dataForPCA = json.load(open('dataPointsResults.txt'))

    #perform PCA
    data, labels = PCA(dataForPCA)

    #plot Graph
    plotGraph(inputFile,data,labels)