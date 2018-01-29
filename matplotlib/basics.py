import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2

# functional
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# row, column, plot you are referring to
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')

# plt.subplot(1,2,2)
# plt.plot(y,x,'b')

# OO
# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# percentage from bottom left
# axes2 = fig.add_axes([0.4, 0.2, 0.4, 0.3])

# axes1.plot(x,y)
# axes1.set_xlabel('X label')
# axes1.set_ylabel('Y label')
# axes1.set_title('Set title')

# axes2.plot(y,x)

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')
print(axes[0])
plt.show()
