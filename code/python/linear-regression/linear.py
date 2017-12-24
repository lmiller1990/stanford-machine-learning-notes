#! /usr/local/bin

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = os.getcwd() + '/population-profit.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
plt.show()

def computeCost(X, y, theta):
    inner = np.power((X * theta.T) - y, 2)
    return np.sum(inner) / (2 * len(X))

# append column of 1s to the data set
data.insert(0, 'Ones', 1)

# set X (training data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:, 0:cols - 1]
y = data.iloc[:, cols - 1:cols]

# convert from data frames to numpy matrix
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0]))

print('X.shape', X.shape, 'theta.shape', theta.shape, 'Y.shape', y.shape)

print(computeCost(X, y, theta))
