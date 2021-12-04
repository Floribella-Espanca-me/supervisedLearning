# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import KNNTester
import NaiveBayesTester
import PerceptronTester
import dataSplitterTester


def main():
    #Exercicio 1 a)
    PerceptronTester.runNORPerceptrons(15,10E-4,30)

    #Exercicio 1 b)
    #PerceptronTester.runORPerceptronsAlpha(15,30,alphaList=[0.5*10E-4,10E-4,2*10E-4,3*10E-4])

    #Exercicio 2
    #KNNTester.runKNN(30,12,klist=[3,7,11,15,19,23])

    #Exercicio 3
    #dataSplitterTester.runDataSplit()

    #Exercicio 4
    #NaiveBayesTester.runNaiveBayes(30,10)
    #NaiveBayesTester.runNaiveBayesGauss(30,10)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
