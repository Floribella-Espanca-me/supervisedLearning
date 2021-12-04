import statistics
from scipy import stats


class IrisDataGaussian:

    def __init__(self,data):
        self.distributions=[]
        self.virginica=[]
        self.setosa=[]
        self.versicolor=[]
        self.virginicaseize=0
        self.setosasize=0
        self.versicolorsize=0
        self.datasize=len(data)

        for i in range(4):
            gauss=[]
            variable=([float(item[i]) for item in data])
            gauss.append(statistics.mean(variable))
            gauss.append(statistics.stdev(variable))
            self.distributions.append(gauss)

        virginicalist=list(filter(lambda c: c[4] == "Iris-virginica", data))
        self.virginicaseize=len(virginicalist)
        for i in range(4):
            gauss = []
            variable = ([float(item[i]) for item in virginicalist])
            gauss.append(statistics.mean(variable))
            gauss.append(statistics.stdev(variable))
            self.virginica.append(gauss)

        versicolorlist = list(filter(lambda c: c[4] == "Iris-versicolor", data))
        self.versicolorsize=len(versicolorlist)
        for i in range(4):
            gauss = []
            variable = ([float(item[i]) for item in versicolorlist])
            gauss.append(statistics.mean(variable))
            gauss.append(statistics.stdev(variable))
            self.versicolor.append(gauss)

        setosalist = list(filter(lambda c: c[4] == "Iris-setosa", data))
        self.setosasize=len(setosalist)
        for i in range(4):
            gauss = []
            variable = ([float(item[i]) for item in setosalist])
            gauss.append(statistics.mean(variable))
            gauss.append(statistics.stdev(variable))
            self.setosa.append(gauss)

        #print("setosa:")
        #print(str(self.setosa))
        #print("versicolor:")
        #print(str(self.versicolor))
        #print("virginica:")
        #print(str(self.virginica))
        #print("global:")
        #print(str(self.distributions))

    def getPclass(self,flowerClass):
        if flowerClass=="Iris-setosa":
            return self.setosasize/self.datasize
        elif flowerClass=="Iris-versicolor":
            return self.versicolorsize /self.datasize
        elif flowerClass=="Iris-virginica":
            return self.virginicaseize / self.datasize


    def getPBbarA(self, sepalL, sepalW, petalL, petalW, flowerclass):
        if flowerclass == "Iris-setosa":
            gauss=self.setosa
        elif flowerclass == "Iris-versicolor":
            gauss = self.versicolor
        elif flowerclass == "Iris-virginica":
            gauss = self.virginica

        if gauss:
            PsepalL = stats.norm(gauss[0][0], gauss[0][1]).pdf(sepalL)
            PsepalW = stats.norm(gauss[1][0], gauss[1][1]).pdf(sepalW)
            PpetalL = stats.norm(gauss[2][0], gauss[2][1]).pdf(petalL)
            PpetalW = stats.norm(gauss[3][0], gauss[3][1]).pdf(petalW)

            #print("floweclass: "+flowerclass)
            #print("gaussian mean:"+str(gauss[0][0]))
            #print("gaussian mean:" + str(gauss[0][1]))
            #print("value: "+str(sepalL))
            #print("P: "+str(PsepalL))
            #print("")
            return PsepalL * PsepalW * PpetalL * PpetalW
        else:
            print("woops")



    def predictClass(self, sepalL, sepalW, petalL, petalW):
        flowerclasses = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        probs = [0, 0, 0]

        for index in range(len(flowerclasses)):
            flowerclass = flowerclasses[index]
            probBbarA=self.getPBbarA(sepalL, sepalW, petalL, petalW,flowerclass)
            probClass=self.getPclass(flowerclass)
            probAbarB = (probBbarA*probClass)
            probs[index] = probAbarB
            #print(probB)
            #print(probBbarA)
            #print(probClass)

        #print(sepalL)
        #print(sepalW)
        #print(petalL)
        #print(petalW)
        #print(str(probs))
        #print(flowerclasses[probs.index(max(probs))])
        return flowerclasses[probs.index(max(probs))]
