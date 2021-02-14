import numpy as np
import matplotlib.pyplot as plt
import math
class computing:
    @property
    def _sigma(self,index,upper,const):#provide sigma for our class
        sum = 0
        for i in range(index,upper+1):
            sum +=const*i
            
    @classmethod
    def CostF(cls,X,Y,theta):#cost function
            m = len(X)
            hypo = theta*X
            sqerror = math.pow((hypo-Y),2)
            J  = 1/(2*m) * cls._sigma(1,m,sqerror)
            get_thetas = lambda theta:np.array([[theta]])
            thetas = list(map(get_thetas,list()))
            for i in len(theta): 
                return "Cost is {a[i]}".format(a = J)  
        # else:
        #     raise ValueError("In 4th argument you can choose your function to be single variable or multi variable:\nFor Single variable:Single(in 4th arg)\nFor Multi variable:Multi")

    @classmethod
    def __init__(cls,sigma):
        cls._sigma = sigma 
        cls.CostF = CostF