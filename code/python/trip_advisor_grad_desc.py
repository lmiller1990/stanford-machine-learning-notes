import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt

def yes_no_to_binary(arr):
    return [1 if val == 'YES' else 0 for val in arr]

def to_int(arr):
    return [int(val) for val in arr]

def to_float(arr):
    return [float(val.replace(',', '.')) for val in arr]

path = os.getcwd() + '/trip_advisor.txt'  
data = pd.read_csv(path, header=None, sep=';')  

# insert row of 1s
data.insert(0, 'Ones', 1)

# separate independent variables X and our dependent variable y
# data.shape = (97, 3) a column of 1s, the independent variable (Population)
# and dependent variable (Profit)
cols = data.shape[1] #=> 3

ones = data[0][1:]
nr_reviews = to_int(data[2][1:])
pool = yes_no_to_binary(data[7][1:])
gym = yes_no_to_binary(data[8][1:])
tennis_court = yes_no_to_binary(data[9][1:])
spa = yes_no_to_binary(data[10][1:])
casino = yes_no_to_binary(data[11][1:])
internet = yes_no_to_binary(data[12][1:])
hotel_stars = to_float(data[14][1:])

print(data.head())
score = data[4][1:]

X = np.matrix([ones, nr_reviews, pool, gym, tennis_court, spa, casino, internet, hotel_stars]).transpose()
y = np.matrix(to_float(score)).transpose()

theta = np.matrix(np.zeros(X.data.shape[1]))
print(X.shape, y.shape)

# convert to numpy matrices
X = np.matrix(X)
y = np.matrix(y)


theta = np.matrix(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])) # seed values for gradient descent

print(X)

def get_cost (X, y, theta):
    # note: np.power will square each elemenet individually, not the entire mat.
    # eg: np.power([1, 2, 3]) = [1, 4, 9], not [1, 2, 3] * [1, 2, 3] which is indeterminant
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradient_descent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape)) # [[0, 0]]
    #print(temp)
    #print(theta.ravel().shape[1])
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

# x = np.linspace(data.Population.min(), data.Population.max(), 100)  
# f = g[0, 0] + (g[0, 1] * x)

a = 5.4
# print(g)

#print(g[0, 0] + g[0,1]*a) # make a prediction

# fig, ax = plt.subplots(figsize=(12,8))
# ax.plot(x, f, 'r', label='Prediction')
# ax.scatter(data.Population, data.Profit, label='Training Data')
# ax.legend(loc=2)

# plt.show()

