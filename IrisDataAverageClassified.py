from statistics import mean


class IrisDataAverageClassified:

    def __init__(self,data):
        self.data=[]
        averages=[]
        for i in range(4):
            averages.append(mean([float(item[i]) for item in data]))
        for flower in data:
            sepalLength= 1 if float(flower[0])>averages[0] else -1
            sepalWidth = 1 if float(flower[1]) > averages[1] else -1
            petalLength = 1 if float(flower[2]) > averages[2] else -1
            petalWidth = 1 if float(flower[3]) > averages[3] else -1
            self.data.append([sepalLength,sepalWidth,petalWidth,petalLength,flower[4]])

        self.setosa=list(filter(lambda c:c[4]=="Iris-setosa" ,self.data))

        self.versicolor = list(filter(lambda c:c[4]=="Iris-versicolor" ,self.data))

        self.virginica = list(filter(lambda c:c[4]=="Iris-virginica" ,self.data))



    def getIrisSetosa(self):
        return self.setosa

    def getIrisVersicolor(self):
        return self.versicolor

    def getIrisVirginica(self):
        return self.virginica

    def getflowerClass(self,flowerClass):
        if flowerClass=="Iris-setosa":
            return self.getIrisSetosa()
        elif flowerClass=="Iris-versicolor":
            return self.getIrisVersicolor()
        elif flowerClass=="Iris-virginica":
            return self.getIrisVirginica()

    def getPattern(self,sepalL,sepalW,petalL,petalW):
        result=[]
        for flower in self.data:
            if flower[0]==sepalL and flower[1]==sepalW and flower[2]==petalL and flower[3]==petalW:
                result.append(flower)
        return result

