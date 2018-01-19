import numpy from np
import pandas as pd
from numpy.random import randn

# seed
np.random.seed(101)

# a dataframe is just a bunch of series.
# a is a series, b, w, x...
df = pd.DataFrame(data=randn(5, 4), index=['a','b','c','d','e'], columns=['w','x','y','z'])

# can query single column (series)
df['w']

# ... multiple returns a dataframe
df[['x','w']]

# df.drop to remove column
df.drop('x', axis=1) # need axis 1. axis=0 refers to a row.

# df.drop needs inplace=true to mutate existing object.
df.drop('x', axis=1, inplace=True)

# remove column, axis=0
df.drop('a')

# get shape. rows x column.
df.shape # (5,4)

# selecting column
df[['w','x']]

# select rows
df.loc['a'] # pass label
# or index
df.iloc[2] # iloc -> index location

df.loc['a','w'] # get specific cell.

# can do more advanced selections.
df.loc[['a','b'], ['w','y']]


