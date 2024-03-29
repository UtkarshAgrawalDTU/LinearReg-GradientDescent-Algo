import numpy as np
import pandas as pd

# Implementation of Gradient Descent Algorithm (Linear Regression for Univariate/Multiple Variables)
# No need to pass x0 = 1 in Dataset matrix (X). Returns theta matrix containing coeffecients of regression line

def LinRegGradientDescent(X, y, alpha = 0.05, iterations = 10000):
    
    X = np.insert(X, 0, values = 1, axis = 1)
    theta = np.zeros(shape = (X.shape[1],1))
    flag = False
    count = 0
    temp = theta
    while flag != True:
        count+=1
        temp = temp - (alpha/m)*(np.dot(X.transpose(), (np.dot(X,theta) - y)))
        
        if np.array_equal(temp, theta) or count >=iterations:
            flag = True
        else:
            theta = temp
    
    return theta


X = np.array([0,1,1,1,1,0,0,0,2,4,4,2,6,0]).reshape(7,2)
Y = np.array([1,2,3,2,0,4,8]).reshape(7,1)
LinRegGradientDescent(X, Y)
