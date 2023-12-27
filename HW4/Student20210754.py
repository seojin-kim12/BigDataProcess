#!/usr/bin/python3

import sys
from os import listdir
import numpy as np
import operator

def createDataSet(dname):
    l = []
    matrix = np.zeros((m, 1024))

    training_list = listdir(dname)
    m = len(training_list)

    for i in range(m):
        file_name = training_list[i]
        answer = int(file_name.split('_')[0])
        l.append(answer)
        matrix[i, :] = getVector(dname + '/' + file_name)
    
    return matrix, l

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def getVector(filename):
    vector = np.zeros((1, 1024))
    with open(filename) as fp:
        for i in range(32):
            line = fp.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
    
    return vector

def main():
    if len(sys.argv) != 3:
        print("python script.py <training_directory> <test_directory>")
        sys.exit(1)

    trainingFile = sys.argv[1]
    testFile = sys.argv[2]

    test_list = listdir(testFile)
    length = len(test_list)
    m, l = createDataSet(trainingFile)

    for k in range(1, 21):
        cnt = 0
        error_cnt = 0
        for i in range(length):
            rst = int(test_list[i].split('_')[0])
            testData = getVector(testFile + '/' + test_list[i])
            c_Result = classify0(testData, m, l, k)

            cnt += 1
            if rst != c_Result:
                error_cnt += 1
        error = (error_cnt / cnt) * 100
        print(f"k = {k}, error = {int(error)}%")

if __name__ == "__main__":
    main()
