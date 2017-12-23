#! /usr/local/bin
import matplotlib.pyplot as plt
import numpy as np
import csv

X = []
y = []

# prepare the data
with open('population-profit.txt', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        feature = [1, float(row[0])] #, float(row[1])]
        y.append(float(row[1]))
        X.append(feature)

m = len(y) # number of training examples

# draw graph
#plt.scatter(X, y)
#plt.show()


# cost

# prepend a columns of ones to x
temp = []
iterations = 1500
alpha = 0.01

for i in range(len(X)):
    temp.append([1])

iterations = 1500
alpha = 0.01

def multiply_matrix(X, y):
    res = []
    i = list(range(len(X)))

    for a in i:
        s = 0
        for val in range(len(b)):
            s += X[a][val] * b[val]
        res.append(s)
    return res

a = [ [1, 2], [3 , 4] ]
b = [ 1, 2 ]

def subtract_one_d(X, y):
    res = []
    iter = 0
    for a in X:
        res = []
        res.append(a - y[iter])
        iter += 1
    return res
    
def subtract(X, y):
    res = []
    iter = 0
    for a in X:
        curr = []
        for b in a:
            curr.append(b - y[iter])
        res.append(curr)
        print(iter)
        iter += 1
    return res
    
def compute_cost(X, y, theta):
    # X * theta
    prediction = multiply_matrix(X, theta)

theta = [0, 0]
print(compute_cost(X, y, theta))
theta = [-1, 2]


