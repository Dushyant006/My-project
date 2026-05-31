#Q1) Combining a one and a two-dimensional NumPy Array 
import numpy as np

a1=np.array([1,2,3])
a2=np.array([[1,2,3],[4,5,6]])
print("One-dimensional array:")

print(a1)
print("Two-dimensional array:")

print(a2) 
con_arr=np.concatenate((a1,a2.flatten()))
print("Combined array:")
print(con_arr)