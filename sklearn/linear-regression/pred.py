import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('USA_Housing.csv')
X = df.drop(['Price', 'Address'], axis=1)
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

# Making a prediction
to_predict = [[66700, 5.7, 8, 4.5, 37000]]
print('Data\n', X_test.iloc[0], '\nPrice', y_test.iloc[0])
print('Data to predict', to_predict, '\nPredicted price', lm.predict(to_predict))

# visualise
predictions = lm.predict(X_test)
# plt.scatter(y_test, predictions)
sns.distplot((y_test - predictions)) # see diff
# plt.show()

# Eval metrics
# Mean Abs Error 
# Mean Sqr Error - punish larger errors
# Root Mean Sqrt Error - interpret in the y units

from sklearn import metrics
mae = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

print('mae', mae, 'mse', mse, 'rmse', rmse)


