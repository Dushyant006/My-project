#Q5) Iterate 3D array using for loop and nditer
import numpy as np
a3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D array:", a3)

for i in np.nditer(a3):
    print(i)

print("\nIterating using nested for loops:")
for i in a3:
    for j in i:
        for k in j:
            print(k)