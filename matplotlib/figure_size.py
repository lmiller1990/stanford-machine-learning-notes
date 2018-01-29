import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(y,x)

plt.show()

fig = plt.figure(figsize=(3,2), dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

plt.show()
# or

# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
# axes[0].plot(x,y)
# axes[1].plot(y,x)

fig = plt.figure()
# fig.savefig('my_fig.png', dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.set_title('My title')
ax.set_ylabel('Y label')
ax.set_xlabel('X label')
ax.plot(x,y)

# plt.tight_layout()

plt.show()
