import numpy as np
#Replace NaN values with average of columns 
arr_with_nan = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
print("\nOriginal Array with NaN:")
print(arr_with_nan)
col_means = np.nanmean(arr_with_nan, axis=0)
inds = np.where(np.isnan(arr_with_nan))
arr_with_nan[inds] = np.take(col_means, inds[1])
print("\nArray after replacing NaN with column averages:")
print(arr_with_nan)