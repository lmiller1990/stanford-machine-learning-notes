#! /usr/local/bin

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model  

def computeCost(X, y, theta):
    inner = np.power((X * theta.T) - y, 2)
    return np.sum(inner) / (2 * len(X))


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y , theta)

    return theta, cost


path = os.getcwd() + '/housing.txt'

data2 = pd.read_csv(path, header=None, names=['Size', 'Bedrooms', 'Price'])

# feature normalization
# subtract from each value the mean of the feature and divide by standard deviation
#data2 = (data2 - data2.mean()) / data2.std()

data2.insert(0, 'ones', 1)
cols = data2.shape[1]
X = data2.iloc[:, 0:cols-1]
y = data2.iloc[:, cols-1:cols]

X = np.matrix(X.values, dtype=np.float128)
y = np.matrix(y.values, dtype=np.float128)
theta = np.matrix(np.array([0, 0, 0]))

# initialize variables for learning rate and iterations
alpha = 0.01  
iters = 1000

# perform gradient descent to "fit" the model parameters

g, cost = gradientDescent(X, y, theta, alpha, iters)


model = linear_model.LinearRegression()  
model.fit(X, y)  

print(model.predict([[1, 1203, 3]]))

prediction = g[0, 0] + (g[0, 1] * 1852) + (g[0, 2] * 4)
# print(g[0, 0] + (g[0, 1] * 12))

print(g, prediction)

