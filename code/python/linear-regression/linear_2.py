import matplotlib.pyplot as plt
import numpy as np
import csv

X = []
y = []
theta = np.array([[0], [0]])

with open('mine.txt', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        feature = [1, float(row[0])]
        X.append(feature)
        y.append([float(row[1])])

# change to np array
X = np.array(X)
y = np.array(y)

# plot it
plt.plot(X, y)
plt.show()

# calculate cost
def computed_cost(X, y, theta):
    prediction = X.dot(theta)
    diff = np.subtract(prediction, y)
    error = np.square(diff)
    sum = np.sum(error)

    return 1 / (2 * y.size) * sum


cost = computed_cost(X, y, theta)

