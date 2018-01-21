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

# comparsion
df(data=[[1,2], [-1, -2]])
df > 0
# 0      1
# 0   True   True
# 1  False  False
df['W'] > 0 # get a series of T/F
# only get the rows that match
df[df['W']>0]

# advanced conditionals.
# need to use & and | instead of and, or
df[(df['Y']>0) & (df['Y'] > 1)]
# W         X         Y         Z
# E  0.190794  1.978757  2.605967  0.683509

# can reset index. df.reset_index(inplace=True)
df.set_index(['','']) # add a new index. Mutates existing DataFrame.

# multi index DataFrame
# pd.MultiIndex.from_tuple(['G1' ..., [1...]])
# MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
#                  labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

df.index.names = ['Groups', 'Num']
#                    A         B
# Groups Num
# G1    1    0.302665  1.693723
#       2   -1.706086 -1.159119
#       3   -0.134841  0.390528
# G2    1    0.166905  0.184502
#       2    0.807706  0.072960
#       3    0.638787  0.329646
df.xs(1, level=1) # Cross section

# A         B
# Groups
# G1      0.302665  1.693723
# G2      0.166905  0.184502

# Missing Data

df = pd.DataFrame({'A': [1, 2, nan], 'B': [5, nan, nan], 'C': [1, 2, 3]})
df.dropna() # drop any rows with nan values
df.dropna(axis=1) # drop any columns with nan values
df.dropna(axis=1, thresh=2) # drop any columns with thresh no. of nan values
df.fillna(value=100) # replace nan with value
df['A'].fillna(value=df['A'].mean()) # replace nan with mean

