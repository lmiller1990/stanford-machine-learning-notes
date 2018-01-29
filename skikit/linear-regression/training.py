import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Get the data
df = pd.read_csv('USA_Housing.csv')

df.head() # see some information
df.describe() # see some stats
df.columns # see column names

sns.pairplot(df) # see a bunch of data
# plt.show()

# dist of target column
sns.distplot(df['Price'])
sns.heatmap(df.corr(), annot=True)

# split data into X and y array - train/target
X = df.drop(['Price', 'Address'], axis=1)
y = df['Price']

X_train, X_Test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

