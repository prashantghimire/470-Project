#!/usr/bin/python
import random
import math

# A method that finds the distance between two collection (eachExample & centroids)


def distanceCalculator(eachExample =None, centroids =None):
    distance = []
    for eachCentroid in centroids:
        list = centroids[eachCentroid]
        temp = 0
        for x in range(0, len(list)-1):
            temp += math.pow(float(eachExample[x]) - float(list[x]), 2)
        distance.append(math.sqrt(temp))
    return distance

# A method that makes a distance matrix of two collection (exampleList & centroids) using distanceCalculator()

def distanceBetween(coordinate, centroid):
    a = 0
    for x in range(0, len(coordinate)):
        a += math.pow(coordinate[x] - centroid[x] ,2)
    return math.sqrt(a)

def distanceList(exampleList = None, centroids = None):
    initialDistance = []
    for eachExample in exampleList:
        distance = []
        for eachCentroid in centroids:
            list = centroids[eachCentroid]
            temp = 0
            for x in range(0, len(list)-1):
                temp += math.pow(float(eachExample[x]) - float(list[x]), 2)
            distance.append(math.sqrt(temp))
        initialDistance.append(distance)
    return initialDistance

# Print function


def printClusters(clusters =None):

    with open('out.txt', 'w') as file:
        for eachCluster in clusters:
            file.write('CLUSTER %s \n' % (eachCluster + 1))
            file.write('\t %s \n' % clusters[eachCluster])

centroids = {}
exampleList, nameOfExample = [], []
count, numOfAttributes, numOfClusters, numOfExamples = 0, 0, 0, 0
# Reading the file
with open('bands.csv') as file:
    for eachLine in file:
        eachLine = eachLine.strip()
        if count == 0:
            numOfExamples = int(eachLine)
        elif count == 1:
            numOfAttributes = int(eachLine)
        elif count == 2:
            numOfClusters = int(eachLine)
        else:
            nameOfExample.append(eachLine.split(',')[0])
            exampleList.append(eachLine.split(',')[1:])
        count += 1
# Choosing centroids
for x in range(0, numOfClusters):
    choice = random.choice(exampleList)
    # TO REMOVE DUPLICATE CENTROIDS
    while choice in centroids.values():
        choice = random.choice(exampleList)
    centroids[x] = choice

initialDistance = distanceList(exampleList, centroids)

iterator = 0
checkCluster = {}
keeperX = 0
keeperY = 0
anotherCluster = {}
final_centroids = {}
cluster_items = {}

while iterator <= math.pow(numOfExamples, 2):
    clusters = {}

    for x in range(0, len(initialDistance)):
        min = initialDistance[x][0]
        keeperY = 0
        keeperX = x
        for y in range(0, len(initialDistance[x])):
            if min > initialDistance[x][y]:
                min = initialDistance[x][y]
                keeperY = y
                keeperX = x
        if keeperY not in clusters.keys():
            clusters[keeperY] = []
            clusters[keeperY].append(nameOfExample[keeperX])
            anotherCluster[keeperY] = []
            anotherCluster[keeperY].append(exampleList[keeperX])
        else:
            anotherCluster[keeperY].append(exampleList[keeperX])
            clusters[keeperY].append(nameOfExample[keeperX])

    m = 0;
    for eachCluster in anotherCluster:
        temp = anotherCluster[eachCluster]
        cluster_items[m] = temp
        m += 1
        tempList = temp[0]
        for x in range(1, len(temp)):
            tempList = [float(x) + float(y) for x, y in zip(temp[x], tempList)]
        tempList[:] = [float(x) / len(temp) for x in tempList]
        centroids[eachCluster] = tempList
    iterator += 1
    if checkCluster == clusters:
        break
    checkCluster = clusters
    final_centroids = centroids
    initialDistance = distanceList(exampleList, centroids)
printClusters(checkCluster)

# print(checkCluster[3][4]) # band name cluster

# print(cluster_items) # coordinates value cluster


float_cluster = []
# print(checkCluster)
# print(len(checkCluster))
# print(cluster_items)
# print(len(cluster_items))


for i in range(0, len(cluster_items)):
    item = (cluster_items.get(i))
    for j in range(0, len(item)):
        temp = []
        for k in range (0, len(item[j])):
            val = float(item[j][k])
            temp.append(val)
        # print(temp)
        print(distanceBetween(temp, final_centroids[i]))
    print("\n")