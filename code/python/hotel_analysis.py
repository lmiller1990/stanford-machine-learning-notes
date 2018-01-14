import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt

def yes_no_to_binary(arr):
    return [1 if val == 'YES' else 0 for val in arr]

path = os.getcwd() + '/trip_advisor.txt'  
data = pd.read_csv(path, header=None, sep=';')  

# insert row of 1s
data.insert(0, 'Ones', 1)

# print(data.head())
nr_reviews = data[2]
pool = yes_no_to_binary(data[7])
gym = yes_no_to_binary(data[8])
tennis_court = yes_no_to_binary(data[9])
spa = yes_no_to_binary(data[10])
casino = yes_no_to_binary(data[11])
internet = yes_no_to_binary(data[12])
hotel_stars = data[14]

# dep variable is score
score = data[4]

X = np.matrix([nr_reviews, pool, gym, tennis_court, spa, casino, internet, hotel_stars]).transpose()
y = np.matrix([score]).transpose()
print(X.shape, y.shape)

theta = np.matrix(np.zeros(X.data.shape[1]))

def get_cost (X, y, theta):
    # note: np.power will square each elemenet individually, not the entire mat.
    # eg: np.power([1, 2, 3]) = [1, 4, 9], not [1, 2, 3] * [1, 2, 3] which is indeterminant
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradient_descent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape)) # [[0, 0]]
    print(temp)
    print(theta.ravel().shape[1])
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

print(g)
