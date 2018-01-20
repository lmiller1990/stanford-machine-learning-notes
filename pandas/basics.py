# pandas is built on top of numpy!
# does data visualation too.
# pip install pandas to install.

## Series
# similar to a numpy array.
# but a series can have axis labels.

import numpy as np
import pandas as pd

ser1 = pd.Series([1, 2, 3])
# 0 1
# 1 2
# 2 3

labels = ['A', 'B', 'C']
my_data = [10, 20, 30]
arr = np.array(my_data) # 10, 20, 30
dict = { 'a': 10, 'b': 20, 'c': 20 }

series = pd.Series(data=my_data)
# 0 10
# 1 20
# 2 30

series = pd.Series(index=labels, data=my_data)
# a 10
# b 20
# c 30

series(arr) # ok. Can pass np.array to data
series(dict) # combines labels and data

s1 = pd.Series(data=[1,2,3], index=['a','b','c'])
s2 = pd.Series(data[2,3,4], index=['b','c','d'])

# you can add them up. Non commom elements are set to NaN.
s1 + s2
# a    NaN
# b    4.0
# c    6.0
# d    NaN

