#Solve the following equation using linalg() and inverse Matrix method x - 2y + 3z = 9 -x + 3y - z = -6 2x - 5y + 5z = 17
import numpy as np
# Coefficient matrix
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
# Right-hand side vector
b = np.array([9, -6, 17])
# Solve for x, y, z
solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)
