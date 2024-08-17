import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as linalg


# Generate a random matrix
n = 1000  # size of the matrix
A = np.random.rand(n, n)
A_normalised= A / np.linalg.norm(A)

# Compute the renormalized transpose
A_transpose = A.T / np.linalg.norm(A.T)

# Compute the product of A and its renormalized transpose
product = np.dot(A_normalised, A_transpose)
print("Product of A and its renormalized transpose:", product)

# Compute the difference between the product and the identity matrix
diff = product - np.eye(n)

# Calculate the Frobenius norm of the difference matrix
norm = np.linalg.norm(diff)

# Print the result
print("Frobenius norm of the difference matrix:", norm)


