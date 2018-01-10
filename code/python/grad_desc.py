import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

y_true = [1, 2, 3]
y_pred = [1, 2, 3]
mse = mean_squared_error(y_true, y_pred)

print(mse)

f, ax = plt.subplots(1)
#x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
#y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]
x = [1, 2, 3]
y0 = [1, 0.5, 0]
y1 = [1, 2, 3]
y2 = [1, 1.5, 2]
y3 = [1, 2.5, 4]
y4 = [1, 3, 5]
y5 = [1, 3.5, 6]
 
_y0 = mean_squared_error(x, y0)
_y1 = mean_squared_error(x, y1)
_y2 = mean_squared_error(x, y2)
_y3 = mean_squared_error(x, y3)
_y4 = mean_squared_error(x, y4)
_y5 = mean_squared_error(x, y5)
# ax.scatter(x, y)
ax.plot(x, y0)
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)
ax.plot(x, y4)
ax.plot(x, y5)

ax.plot(-0.5, _y0, marker='x', markersize=3, color="red")
ax.plot(1, _y1, marker='x', markersize=3, color="red")
ax.plot(0.5, _y2, marker='x', markersize=3, color="red")
ax.plot(1.5, _y3, marker='x', markersize=3, color="red")
ax.plot(2, _y4, marker='x', markersize=3, color="red")
ax.plot(2.5, _y5, marker='x', markersize=3, color="red")

ax.plot([-0.5, 0.5, 1, 1.5, 2, 2.5], [_y0, _y2, _y1, _y3, _y4, _y5])

ax.set_xlabel('theta1') 
ax.set_ylabel('J(theta1)') 

ax.set_ylim(ymin=0, ymax=4)
ax.set_xlim(xmin=0, xmax=4)
plt.show()


