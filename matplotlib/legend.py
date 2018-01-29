import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(1,5,11)
x = y ** 2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x, label='X and X')
ax.plot(x,y, label='X and Y')
ax.set_title(label='My plot')

ax.legend()
plt.show()
