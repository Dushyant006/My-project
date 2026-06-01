#Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]]
import numpy as np
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
print("Original Array:")
print(arr)
# Replace NaN with 0
arr = np.nan_to_num(arr)
print("\nArray after replacing NaN with 0:")
print(arr)
# Interchange rows and first 3 columns
if arr.shape[0] >= 3:
    arr[[0, 1, 2]] = arr[[2, 0, 1]]
else:
    arr[[0, 1]] = arr[[1, 0]]
arr[:, [0, 1, 2]] = arr[:, [2, 0, 1]]
print("\nArray after interchanging rows and columns:")
print(arr)