import matplotlib.pyplot as plt
import numpy as np  
import math

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

def negative_log(x):
    return np.log(x) * -1

def one_minus_negative_log(x):
    return np.log(1-x) * -1

x = np.linspace(-50, 50, 10)  
f = list(map(sigmoid, x))

x = np.linspace(-1, 1, 100, endpoint=True)
# or we can use x = np.arrange(-1, 1, step=0.1)
# y = np.sqrt(-x**2. + 0.6)

# plt.plot(x, y)
# plt.plot(x, -y)

fig, ax = plt.subplots(2, 2)
# ax.plot(x, list(map(sigmoid, x)), 'r')
ax[0, 0].plot(x, list(map(negative_log, x)), 'r')
ax[0, 1].plot(x, list(map(one_minus_negative_log, x)), 'r')

plt.show()
