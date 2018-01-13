import matplotlib.pyplot as plt
import numpy as np  
import math

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 100)  
f = list(map(sigmoid, x))

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r')

plt.show()
