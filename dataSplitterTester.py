import KNNTester
import dataSplitter


def runDataSplit():
    data=KNNTester.importfile()
    indexlabel=("Sepal Length","Sepal width","Petal length","Petal width")
    for index in range(4):
        print("Information gain of split by "+indexlabel[index]+":")
        print(dataSplitter.calcGain(data,index))
        print("")
