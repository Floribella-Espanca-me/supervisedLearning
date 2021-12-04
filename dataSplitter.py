import math
from statistics import mean


def splitData(data,index):
    valueList=[float(item[index]) for item in data]
    average=mean(valueList)
    dataSplit1=list(filter(lambda item:float(item[index])<=average,data))
    dataSplit2 = list(filter(lambda item: float(item[index]) > average, data))
    return [dataSplit1,dataSplit2]


def countIrisSetosa(data):
    valuelist=[item[4] for item in data]
    return valuelist.count("Iris-setosa")

def countNOTIrisSetosa(data):
    return len(data)-countIrisSetosa(data)

def calcEntropy(data):
    pplus=countIrisSetosa(data)/len(data)
    pminus=countNOTIrisSetosa(data)/len(data)
    if (pplus==0) or (pminus==0):
        return 0
    else:
        return -((pplus*math.log(pplus,2))+(pminus*math.log(pminus,2)))

def calcGain(data,index):
    splits=splitData(data,index)
    SvSum=0
    for split in splits:
        SvSum= SvSum + len(split)*calcEntropy(split)
    return calcEntropy(data)-(SvSum/len(data))