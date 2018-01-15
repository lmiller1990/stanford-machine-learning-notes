import numpy as np

# indexing and selection
arr = np.arange(0,11) # array([1,2 ....10])
arr[1] # 1
arr[1:5] # 1, 2, 3, 4, 5
arr[:6] # everything up to position 6
arr[1:] # every from 1 to the end

arr[0:5] = 100

slice_of_arr = arr[0:6] # 0 1 2 3 4 5

# broadcast - by reference, not copy.
slice_of_arr[:] = 99

# to get copy
arr_copy = arr.copy()

arr_copy[:] = 200

# arr_copy = [200, 200...]
# arr [99, 99,...6 7 8]

arr_2d = np.array([[5,10,15],[20,25,30], [35,40,45]])

arr_2d[1] # 5
arr_2d[0][0] # 5
arr_2d[0, 0] # 5
arr_2d[:2,1:] # [[10, 15],[25,30]]

# conditional selection
arr = arange(0, 10)
arr > 5 # [6, 7 ... 10]
arr[arr>5] # [6, 7 ... 10]
arr[arr<3] # [1, 2]

# operations

## scalar
arr = np.arange(0,10)
arr+arr # [2, 4 , 6...]
arr+1 = # [1, 2, 3] # all elems increase by 1
arr/2 = # [.5, 1, 1.5...]
arr ** 2 # [1, 4, 9...]

## universal functions, (ufunc)
np.sqrt(arr) # 1, 1.41..
np.exp(arr)
np.max(arr) # get max 
np.sin(arr) 

