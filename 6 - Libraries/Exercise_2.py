import numpy as np

A = np.array([[5, 6], [9, 8]])
B = np.array([[7, 2], [6, 3]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
print("A + B:\n", A + B)
# Matrix multiplication
print("A x B:\n", np.dot(A, B))
# Transpose of A
print("Transpose of A:\n", A.T)
# Element-wise multiplication
print("Element-wise A * B:\n", A * B)