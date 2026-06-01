import numpy as np
#Move axes of 3D array to new positions
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nOriginal 3D Array:")
print(arr_3d)
arr_3d = np.moveaxis(arr_3d, 0, 2)
print("\nArray after moving axes:")
print(arr_3d)