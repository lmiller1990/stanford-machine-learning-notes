import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt

path = os.getcwd() + '/food_dataset.txt'  
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])  

# insert row of 1s
data.insert(0, 'Ones', 1)

# separate independent variables X and our dependent variable y
# data.shape = (97, 3) a column of 1s, the independent variable (Population)
# and dependent variable (Profit)
cols = data.shape[1] #=> 3

X = data.iloc[:, 0:cols-1] # The first column of 1s and Population data
y = data.iloc[:, cols-1:cols] # the Profit column data

# convert to numpy matrices
X = np.matrix(X.values)
y = np.matrix(y.values)

theta = np.matrix(np.array([0, 0])) # seed values for gradient descent

def get_cost (X, y, theta):
    # note: np.power will square each elemenet individually, not the entire mat.
    # eg: np.power([1, 2, 3]) = [1, 4, 9], not [1, 2, 3] * [1, 2, 3] which is indeterminant
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradient_descent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape)) # [[0, 0]]
    parameters = int(theta.ravel().shape[1]) # 2, number of params
    cost = np.zeros(iters) # cost - should get closer to  0 as we go

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))


        theta = temp
        cost[i] = get_cost(X, y, theta)

    return theta, cost

alpha = 0.01
iters = 1000

g, cost = gradient_descent(X, y, theta, alpha, iters)  

x = np.linspace(data.Population.min(), data.Population.max(), 100)  
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Training Data')
ax.legend(loc=2)

plt.show()

