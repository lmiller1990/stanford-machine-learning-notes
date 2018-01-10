import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt

path = os.getcwd() + '/food_dataset.txt'  
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])  

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))  
# plt.show()

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

cost = get_cost(X, y, theta)

print(cost)

