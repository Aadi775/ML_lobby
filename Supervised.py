import numpy as np
import matplotlib.pyplot as plt
import math
class computing:
    def plot(x,y):
        plt.lablex("X")
        plt.labley("Y")
        plt.plot(x,y)
    
    @property
    @classmethod
    def _sigmoid(cls,x, y,theta):
        e = math.pow(1+1/n,n)
        hypo = np.transpose(theta)*x
        g = 1/1+math.pow(hypo)
        

    @property
    def _sigma(self,index,upper,const):#provide sigma for our class
        sum = 0
        for i in range(index,upper+1):
            sum +=const*i
            
    @classmethod
    def CostF(cls,X,Y,theta):#cost function
        try:
            for e in range(len(X)):
                m = len(X)
                hypo = theta*X[e]
                sqerror = math.pow((hypo-Y[e]),2)
                J  = 1/(2*m) * cls._sigma(1,m,sqerror)
                get_thetas = lambda theta:np.array([[theta]])
                thetas = list(map(get_thetas,list()))
                for i in len(theta): 
                    return "Cost is {a[i]}".format(a = J)  
        except Exception as e:
            if e == "TypeError":
                raise ValueError("X and Y must be list and of same dimension")
        # else:
        #     raise ValueError("In 4th argument you can choose your function to be single variable or multi variable:\nFor Single variable:Single(in 4th arg)\nFor Multi variable:Multi")

    @classmethod
    def Gradientdescent(x, y,theta,alpha,iters):
        m = np.length(y)
        J_history = np.zeros(iters,1)
        for i in range(iters):
            error =(x*theta)-y
            theta = theta-((alpha/m)*np.transpose(x)*error)
            a = []
            a.append(theta)
        return J_history,theta




    @classmethod
    def __init__(cls,sigma,sigmoid,CostF,Gradientdescent):
        cls._sigma = sigma 
        cls.CostF = CostF
        cls.Gradientdescent = GradientDescent
        cls._sigmoid = sigmoid 


class cllasification(computing):
    def __init__(self):
        super().__init__()
        self.Gradientdescent = Gradientdescentclas()

    @property
    def Gradientdescentclas(self,x,y,theta):
        m = len(x)
        for i in len(range(x)):
            e = math.pow(1+1/n,n)
            hypo = np.transpose(theta)*x
            g = 1/1+math.pow(hypo)

            clas_term = -y[i]*np.log(hypo*(x[i]))-(1-y[i])*log(1-hypo*(x[i]))
            J = 1/m*computing._sigma(1,m,clas_term)

    @property
    def regCostF(self,x,y,theta):
        m = len(x)
        for i in len(range(x)):
            e = math.pow(1+1/n,n)
            hypo = np.transpose(theta)*x
            g = 1/1+math.pow(hypo)                
            # regterm
            clas_term = -y[i]*np.log(hypo*(x[i]))-(1-y[i])*log(1-hypo*(x[i]))
            J = 1/m*computing._sigma(1,m,clas_term)
    
