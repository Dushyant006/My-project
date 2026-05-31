#Q4) Practice operations like 
#   i)Get the maximum value from given array
#   ii) Get the minimum value from given array 
#   iii) Find the number of rows and columns of a given array using NumPy
#   iv) Select the elements from a given array (each element and specific element)
#   v) Find the sum of values in a 2D array using for loop
#   vi) Adding, Subtracting, multiplying, dividing arrays in Numpy
import numpy as np

arr=np.array([1,2,23,3,34,33,234,32])

print("\nMaximum value in the array:", np.max(arr))
print("\nMinimum value in the array:", np.min(arr))

arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print("\nNumber of (rows,columns) in the array:", arr1.shape)

print("\nSelecting elements at specific position:")
print("element at index (0,1):", arr1[0,1])
print("element at index (1,2):", arr1[1,2])


arr2=np.array([[1,2,3],[4,5,6]])
sum=0
for i in np.nditer(arr2):
    sum+=i
print("\nSum of values in the 2D array:", sum)

a1=np.array([1,2,3])
a2=np.array([4,5,6])
print("\nAddition of arrays:", np.add(a1,a2))
print("\nSubtraction of arrays:", np.subtract(a1,a2))
print("\nMultiplication of arrays:", np.multiply(a1,a2))
print("\nDivision of arrays:", np.divide(a1,a2))