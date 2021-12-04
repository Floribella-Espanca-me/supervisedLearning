from collections import Counter

from numpy import sort


class KNN:

    def __init__(self,data,k):
        if k>len(data):
            print("woops")
        else:
            self.data=data
            self.k=k

    @staticmethod
    def distance(flower1,flower2):
        return abs(float(flower1[0])-float(flower2[0]))+abs(float(flower1[1])-float(flower2[1]))+abs(float(flower1[2])-float(flower2[2]))+abs(float(flower1[3])-float(flower2[3]))

    def kclosest(self,flower):
        def distancetoflower(flower1):
            return KNN.distance(flower1,flower)
        self.data.sort(key=distancetoflower)
        return self.data[:self.k]

    def runKNN(self,flower):
        kclose=[item[4] for item in self.kclosest(flower)]
        flowerCount=dict(Counter(kclose))
        return sorted(flowerCount,key=flowerCount.get,reverse=True)[0]


