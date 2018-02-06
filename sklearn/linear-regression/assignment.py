import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv('ecommerce_data')

print(customers.describe())
print(customers.info())

# compare time on website and yearly amount spent
# sns.jointplot(data=customers, x='Time on Website', y='Yearly Amount Spent')

# compare time on website and time on app
# sns.jointplot(data=customers, x='Time on App', y='Yearly Amount Spent')

# compare time on app and length of membership
# sns.jointplot(data=customers, x='Time on App', y='Length of Membership', kind='hex')

# pairplot of all data
# fig = sns.pairplot(customers)
# fig.savefig('pairplot.png', dpi=100)

# linear plot of yearly amt spent vs length of membership
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)

plt.show()

