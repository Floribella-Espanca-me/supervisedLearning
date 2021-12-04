import random
import statistics

import matplotlib.pyplot as plt

from Perceptron import Perceptron


def runORPerceptron(seed,alpha):
    nextseed=seed
    random.seed(nextseed)
    w0=random.random()
    w1=random.random()
    w2=random.random()
    nextseed=w2
    perceptron=Perceptron(w0,w1,w2)
    #print(str(perceptron))

    bitCombinations=[[-1,-1],[-1,1],[1,1],[1,-1]]
    #OR
    dList=[-1,1,1,1]

    right=False
    epoch=0
    while not right:
        epoch+=1
        right=True
        deltaw0 = 0
        deltaw1 = 0
        deltaw2 = 0
        for paternIndex in range(len(bitCombinations)):
            bits=bitCombinations[paternIndex]
            o=perceptron.o(bits[0],bits[1])
            d=dList[paternIndex]
            deltaw0=updateTerm(deltaw0,o,d,alpha,1)
            deltaw1 = updateTerm(deltaw1, o, d, alpha, bits[0])
            deltaw2 = updateTerm(deltaw2, o, d, alpha, bits[1])
            if(o!=d):
                right=False
            perceptron.updateValues(deltaw0,deltaw1,deltaw2)

        #print(o)
        #print(deltaw0)
    return [epoch,nextseed]

def runNORPerceptrons(seed,alpha,Nruns):
    nextseed=seed
    epochList=[]
    for n in range(Nruns):
        exe=runORPerceptron(nextseed,alpha)
        nextseed=exe[1]
        epochList.append(exe[0])

    singleListStatistic(epochList,alpha)
    return [epochList,nextseed]



def runORPerceptronsAlpha(seed,Nruns,alphaList):
    nextseed=seed

    epochListPerAlpha=[]
    for alpha in alphaList:
        exe=runNORPerceptrons(nextseed,alpha,Nruns)
        nextseed=exe[1]
        epochListPerAlpha.append(exe[0])
    #print(str(epochListPerAlpha))
    alphaVarBoxPlot(epochListPerAlpha,alphaList)


def updateTerm(deltaw,o,d,alpha,bit):
    return deltaw+alpha*bit*(d-o)

def boxplotSingle(list):
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(list)
    plt.show()

def singleListStatistic(list,alpha):
    print("Sample with learning-rate "+str(alpha))
    print("Mean of the sample is % s " % (statistics.mean(list)))
    print("Standard Deviation of the sample is % s "%(statistics.stdev(list)))
    print("")

def alphaVarBoxPlot(epochListPerAlpha,alphaList):
    fig, ax = plt.subplots()
    ax.boxplot(epochListPerAlpha)
    ax.set_xticklabels(alphaList)
    plt.xlabel("value of alpha")
    plt.ylabel("# of epochs to converge")
    plt.show()