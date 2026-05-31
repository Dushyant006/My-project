#Create numpy array and perform following operation
#Convert 1D array to 2D 
import numpy as np
a1=np.array([1,2,3,4,5,6])
print("Original array:")
print(a1)
a2=a1.reshape(2,3)
print("\nReshaped array (2D):")
print(a2)

#Print Array Attributes(Like shape, dimenssion, data type, itemsize)
print("\nArray Attributes:")
print("Shape:", a2.shape)
print("Dimensions:", a2.ndim)
print("Data Type:", a2.dtype)
print("Item Size:", a2.itemsize)

#Create a 3×3 NumPy array of all 9
a3=np.full((3,3), 9)
print("\n3×3 array of all 9:")
print(a3)

#Create a 1D array of 10 evenly spaced values between 25 and 125
a4=np.linspace(25, 125, 10)
print("\n1D array of 10 evenly spaced values between 25 and 125:")
print(a4)

#Convert a Python list into a NumPy array
python_list=[1, 2, 3, 4, 5]
a5=np.array(python_list)
print("\nPython list converted to NumPy array:")
print(a5)

#Reverse a 1D NumPy array
a6=a5[::-1]
print("\nReversed 1D NumPy array:")
print(a6)

#Create a 4×4×3 array and extract value at its second set, first row and last column
a7=np.random.rand(4,4,3)
print("\n4×4×3 array:")
print(a7)
extracted_value=a7[1,0,-1]
print("\nExtracted value at second set, first row and last column:", extracted_value)

#Create a 4×4 and Extract Odd Rows and Even Columns
a8=np.random.rand(4,4)
print("\n4×4 array:")
print(a8)
odd_rows=a8[1::2]
print("\nOdd rows:")
print(odd_rows)
even_columns=a8[:, ::2]
print("\nEven columns:")
print(even_columns)

#Slice the first two rows and first two columns of econd set from a 4×4×3 array\
a9=np.random.rand(4,4,3)
print("\n4×4×3 array:")
print(a9)
sliced_array=a9[1, :2, :2]
print("\nSliced array (first two rows and first two columns of second set):")
print(sliced_array)

#Replace all odd numbers in a NumPy array with -1 by itterating using for loop [[23, 56, 78, 93], [71, 82,13, 24]]
a10=np.array([[23, 56, 78, 93], [71, 82,13, 24]])
print("\nOriginal array:")
print(a10)
for i in range(a10.shape[0]):
    for j in range(a10.shape[1]):
        if a10[i, j] % 2 != 0:
            a10[i, j] = -1
print("\nArray after replacing odd numbers with -1:")
print(a10)

#Get the indices of non-zero elements in an array [1, 0, 2, 0, 3, 0, 4]
a11=np.array([1, 0, 2, 0, 3, 0, 4])
print("\nArray:")
print(a11)
indices=np.nonzero(a11)
print("Indices of non-zero elements:", indices[0])

#Perform arithmetic operations on two NumPy arrays element-wise Add two NumPy arrays element by element. Multiply two NumPy arrays element by element.
a12=np.array([1, 2, 3])
a13=np.array([4, 5, 6])
print("\nArray 1:")
print(a12)
print("Array 2:")
print(a13)
sum_arrays=a12 + a13
product_arrays=a12 * a13
print("Sum of arrays:")
print(sum_arrays)
print("Product of arrays:")
print(product_arrays)

#Write a code to compute the dot product of two NumPy arrays arr1 = [15, 20, 25] arr2 = [10,40,37]
arr1=np.array([15, 20, 25])
arr2=np.array([10, 40, 37])
dot_product=np.dot(arr1, arr2)
print("\nDot product of arr1 and arr2:", dot_product)
