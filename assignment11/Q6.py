#Q6) Study the following program import numpy as np # create a numpy 1d-arrays arr1 = np.array([3, 4]) arr2 = np.array([1, 0]) # find average of NumPy arrays avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg) -> Calculate average mean median mode values of two NumPy 2d-arrays

import numpy as np
arr1=np.array([3,4])
arr2=np.array([1,0])
avg=(arr1+arr2)/2
print("Average of NumPy arrays:\n", avg)

arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6],[7,8]])
mean=np.mean(arr3)
median=np.median(arr4)
print("Mean of arr3:", mean)
print("Median of arr4:", median)