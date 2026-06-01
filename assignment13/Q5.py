# Study the following program import numpy as np 
# create a numpy 1d-arrays arr1 = np.array([3, 4]) arr2 = np.array([1, 0]) 
# find average of NumPy arrays avg = (arr1 + arr2) / 2 print("Average of NumPy arrays:\n", avg) -> Calculate average mean median mode values of two NumPy 2d-arrays

import numpy as np
# Create two 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Calculate average
avg = (arr1 + arr2) / 2
print("Average of the two 2D arrays:\n", avg)

# Calculate mean
mean_arr1 = np.mean(arr1)
mean_arr2 = np.mean(arr2)
print("\nMean of arr1:", mean_arr1)
print("Mean of arr2:", mean_arr2)

# Calculate median
median_arr1 = np.median(arr1)
median_arr2 = np.median(arr2)
print("\nMedian of arr1:", median_arr1)
print("Median of arr2:", median_arr2)

# Calculate mode
from scipy import stats
mode_arr1 = stats.mode(arr1, axis=None)[0][0]
mode_arr2 = stats.mode(arr2, axis=None)[0][0]
print("\nMode of arr1:", mode_arr1)
print("Mode of arr2:", mode_arr2)
