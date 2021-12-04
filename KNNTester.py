import random

import pandas as pd
import csv

from matplotlib import pyplot as plt

from KNN import KNN


def importfile():
    with open('iris.data', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def runKNN(nruns,seed,klist):
    nextseed=seed
    klistAccuracyList=[]
    for k in klist:
        kAccuracyList=[]
        for run in range(nruns):
            random.seed(nextseed)
            data=importfile()
            random.shuffle(data)
            nextseed=random.random()
            index=int(len(data)*0.7)
            training=data[:index]
            test=data[index:]
            knn=KNN(training,k)

            correctCounter=0
            for flower in test:
                flowerType=knn.runKNN(flower)
                if(flowerType==flower[4]):
                    correctCounter+=1
            accuracy= correctCounter / len(test)
            kAccuracyList.append(accuracy)
        klistAccuracyList.append(kAccuracyList)
    printResult(klist,klistAccuracyList)

def printResult(kList,kaccuracyList):
    fig, ax = plt.subplots()
    ax.boxplot(kaccuracyList)
    ax.set_xticklabels(kList)
    plt.ylabel("guess accuracy")
    plt.xlabel("value of k")
    plt.show()


