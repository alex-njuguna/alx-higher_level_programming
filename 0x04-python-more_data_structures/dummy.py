def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    squared_matrix = [[0] * len(row) for row in matrix]

    # Iterate over the elements of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square each element and store it in the corresponding position of the new matrix
            squared_matrix[i][j] = matrix[i][j] ** 2

    # Return the squared matrix
    return squared_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)