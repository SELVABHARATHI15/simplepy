import numpy as np
A = np.array([[4, 10, 30],
              [10, 30, 100],
              [30, 100, 354]])
A_inv = np.linalg.inv(A)
print("Inverse of the matrix:")
print(A_inv)
