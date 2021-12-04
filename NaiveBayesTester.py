import random

from matplotlib import pyplot as plt
from scipy import stats

import KNNTester
import NaiveBayes
from IrisDataAverageClassified import IrisDataAverageClassified
from IrisDataGaussian import IrisDataGaussian


def runNaiveBayes(nruns,seed):
    nextseed = seed
    AccuracyList = []
    for run in range(nruns):
        random.seed(nextseed)
        data = KNNTester.importfile()
        random.shuffle(data)
        nextseed = random.random()
        index = int(len(data) * 0.7)
        training = data[:index]
        test = data[index:]

        trainingParsed=IrisDataAverageClassified(training)
        testParsed = IrisDataAverageClassified(test)

        correctCounter = 0
        for flower in testParsed.data:
            flowerType = NaiveBayes.predictClass(trainingParsed,flower[0],flower[1],flower[2],flower[3])
            if (flowerType == flower[4]):
                correctCounter += 1
        accuracy = correctCounter / len(testParsed.data)
        AccuracyList.append(accuracy)
    printResult(AccuracyList)


def printResult(kaccuracyList):
    fig, ax = plt.subplots()
    ax.boxplot(kaccuracyList)
    plt.ylabel("guess accuracy")
    plt.xlabel("NaiveBayes (30 runs)")
    plt.show()

def runNaiveBayesGauss(nruns,seed):
    nextseed = seed
    AccuracyList = []
    for run in range(nruns):
        random.seed(nextseed)
        data = KNNTester.importfile()
        random.shuffle(data)
        nextseed = random.random()
        index = int(len(data) * 0.7)
        training = data[:index]
        test = data[index:]

        trainingParsed=IrisDataGaussian(training)

        correctCounter = 0
        for flower in test:
            sepalL=float(flower[0])
            sepalW=float(flower[1])
            petalL=float(flower[2])
            petalW=float(flower[3])
            flowerType=trainingParsed.predictClass(sepalL,sepalW,petalL,petalW)
            if (flowerType == flower[4]):
                correctCounter += 1
        accuracy = correctCounter / len(test)
        AccuracyList.append(accuracy)
    printResult2(AccuracyList)

def printResult2(kaccuracyList):
    fig, ax = plt.subplots()
    ax.boxplot(kaccuracyList)
    plt.ylabel("guess accuracy")
    plt.xlabel("NaiveBayes Gaussian(30 runs)")
    plt.show()


def debug(nruns, seed):
    nextseed = seed
    AccuracyList = []

    random.seed(nextseed)
    data = KNNTester.importfile()
    random.shuffle(data)
    nextseed = random.random()
    index = int(len(data) * 0.7)
    training = data[:index]
    test = data[index:]

    trainingParsed = IrisDataGaussian(data)

    correctCounter = 0

    flower=test[0]
    sepalL = float(flower[0])
    sepalW = float(flower[1])
    petalL = float(flower[2])
    petalW = float(flower[2])
    flowerType = trainingParsed.predictClass(sepalL, sepalW, petalL, petalW)

    print(stats.norm(0,1).pdf(1))

    print(flowerType)

