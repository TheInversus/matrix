import numpy as np
# Get the number of rows and columns for the matrix
rows, columns = map(int, input("Enter the number of rows and columns for the matrix (separated by a space): ").split())

# Initialize an empty matrix
matrix = []

# Get the values for the matrix
for i in range(rows):
    matrix.append(list(map(int, input("Enter the values for row {} (separated by spaces): ".format(i+1)).split())))

# Print the matrix
for row in matrix:
    print(row)

# Define the matrix
matrix = np.array(matrix)
# Find the transpose of the matrix
transpose = np.transpose(matrix)
print("Transpose: \n", transpose)




if rows==columns:
    # Find the inverse of the matrix
    inverse = np.linalg.inv(matrix)
    print("Inverse: \n", inverse)
    
    # Find the determinant of the matrix
    determinant = np.linalg.det(matrix)
    print("Determinant: ", determinant)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # Print the results
    print("Eigenvalues: ", eigenvalues)
    print("Eigenvectors: \n", eigenvectors)

else:
    print("Inverse AND eigenvalue/eigenvectors can only be obtained for squared matrix.")
