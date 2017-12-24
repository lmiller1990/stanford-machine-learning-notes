import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn import linear_model  

path = os.getcwd() + '/population-profit.txt'  
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])  
data.head()  
# append a ones column to the front of the data set
data.insert(0, 'Ones', 1)

# set X (training data) and y (target variable)
cols = data.shape[1]  
X = data.iloc[:,0:cols-1]  
y = data.iloc[:,cols-1:cols]  
# convert from data frames to numpy matrices
X = np.matrix(X.values)  
y = np.matrix(y.values)  

model = linear_model.LinearRegression()  
model.fit(X, y)  

print(model.predict([[1, 5.4]]))

