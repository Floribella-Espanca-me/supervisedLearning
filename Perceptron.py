class Perceptron:


    def __init__(self,w0,w1,w2):
        self.w0=w0
        self.w1=w1
        self.w2=w2

    def f(self,x):
        if x<=0:
            return -1
        else:
            return 1

    def o(self,x1,x2):
        return self.f(self.w0+self.w1*x1+self.w2*x2)

    def updateValues(self,deltaw0,deltaw1,deltaw2):
        self.w0=self.w0+deltaw0
        self.w1=self.w1+deltaw1
        self.w2=self.w2+deltaw2

    def __str__(self):
        return "w0: "+str(self.w0)+"\nw1: "+str(self.w1)+"\nw2: "+str(self.w2)+"\n"