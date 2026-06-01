import numpy as np
#Replace negative value with zero in numpy array using replace 
arr_with_negatives = np.array([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
print("\nOriginal Array with Negatives:")
print(arr_with_negatives)
arr_with_negatives[arr_with_negatives < 0] = 0
print("\nArray after replacing negative values with zero:")
print(arr_with_negatives)