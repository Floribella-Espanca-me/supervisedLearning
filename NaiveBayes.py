
def countValueInX(dataX,value,index):
    if not -1<index<4:
        print("algo de errado nao esta certo")
    else:
        count=0
        for flower in dataX:
            if flower[index]==value:
                count+=1
        return count


def getPBbarA(data,sepalL,sepalW,petalL,petalW,flowerclass):
    classobservations=data.getflowerClass(flowerclass)
    sepalLcount=countValueInX(classobservations,sepalL,0)
    sepalWcount=countValueInX(classobservations,sepalW,1)
    petalLcount=countValueInX(classobservations,petalL,2)
    petalWcount=countValueInX(classobservations,petalW,3)
    size=len(classobservations)
    return (sepalLcount/size)*(sepalWcount/size)*(petalLcount/size)*(petalWcount/size)

def getPA(data,flowerclass):
    classobservations = data.getflowerClass(flowerclass)
    return len(classobservations)/len(data.data)

def getPX(data,sepalL,sepalW,petalL,petalW):
    samePattern=data.getPattern(sepalL,sepalW,petalL,petalW)
    return len(samePattern)/len(data.data)

def predictClass(data,sepalL,sepalW,petalL,petalW):
    flowerclasses=["Iris-setosa","Iris-versicolor","Iris-virginica"]
    probs=[0,0,0]
    probB=getPX(data,sepalL,sepalW,petalL,petalW)
    if probB==0: probB=1

    for index in range(len(flowerclasses)):
        flowerclass=flowerclasses[index]
        probAbarB=((getPBbarA(data,sepalL,sepalW,petalL,petalW,flowerclass))*(getPA(data,flowerclass)))/probB
        probs[index]=probAbarB

    return flowerclasses[probs.index(max(probs))]