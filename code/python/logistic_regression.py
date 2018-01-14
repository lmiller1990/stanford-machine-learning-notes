import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt
import scipy.optimize as opt  


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    # hypothesis is sigmoid where z = theta.T * x
    first = np.multiply(y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first + second) / -len(X)

path = os.getcwd() + '/exams_data.txt'  
data = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])  


positive = data[data['Admitted'].isin([1])]
negative = data[data['Admitted'].isin([0])]
data.insert(0, 'Ones', 1)

cols = data.shape[1]  
X = data.iloc[:,0:cols-1]  
y = data.iloc[:,cols-1:cols]

# convert to numpy arrays and initalize the parameter array theta
X = np.array(X.values)  
y = np.array(y.values)  
theta = np.zeros(3) 

def gradient(theta, X, y):  
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        term = np.multiply(error, X[:,i])
        grad[i] = np.sum(term) / len(X)

    return grad

def predict(theta, X):  
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]

result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))  
theta_min = np.matrix(result[0])  
cost(result[0], X, y)  
predictions = predict(theta_min, X) 

correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]  
accuracy = (sum(map(int, correct)) % len(correct))  
print('accuracy = {0}%'.format(accuracy))
# print(predict(theta_min, [1 ,70, 60]))

# fig, ax = plt.subplots()
# ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
# ax.scatter(negative['Exam 1'], negative['Exam 2'], s=10, c='r', marker='x', label='Not admitted')
# ax.legend()
# plt.show()

