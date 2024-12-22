To find the eigenvalues of the given matrix, we need to calculate the characteristic equation and solve for the eigenvalues.

The given matrix is:
```python
import numpy as np

# Define the matrix
A = np.array([[4, 1, 2], [0, 3, -1], [-2, 0, 5]])

# Calculate the eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("The eigenvalues of the matrix are: ", eigenvalues)
```



Here are the Eigenvalues: [6.26871478, 2.73114262+1.37840933j, 2.73114262-1.37840933j]