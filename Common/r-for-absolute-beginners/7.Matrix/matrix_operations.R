example_matrix_1 <- matrix(1:4, nrow = 2, ncol = 2)
example_matrix_2 <- matrix(200:303, nrow = 2, ncol = 2)

example_matrix_1
example_matrix_2

example_matrix_1*example_matrix_2

example_matrix_3 <- matrix(200:205, nrow = 2, ncol = 3)
example_matrix_3

# example_matrix_1*example_matrix_3
# Error in example_matrix_1 * example_matrix_3 : non-conformable arrays

example_matrix_4 <- matrix(200:205, nrow = 3, ncol = 2)
# example_matrix_1*example_matrix_4
# Error in example_matrix_1 * example_matrix_4 : non-conformable arrays

dim(example_matrix_4)
dim(example_matrix_1)
dim(example_matrix_2)
example_matrix_1-example_matrix_2

matrix_1 <- matrix(1:6, nrow = 2, ncol = 3, byrow = TRUE)
matrix_2 <- matrix(7:12, nrow = 3, ncol = 2, byrow = TRUE)

# matrix_1*matrix_2
# Error in matrix_1 * matrix_2 : non-conformable arrays

# Dot product:
matrix_1 %*% matrix_2

dim(matrix_1)
dim(matrix_2)


matrix_1 <- matrix(1:6, nrow = 2, ncol = 12, byrow = TRUE)
matrix_2 <- matrix(7:12, nrow = 3, ncol = 2, byrow = TRUE)

dim(matrix_1)
dim(matrix_2)
# matrix_1 %*% matrix_2
# Error in matrix_1 %*% matrix_2 : non-conformable arguments



matrix_1 <- matrix(1:6, nrow = 202, ncol = 3, byrow = TRUE)
matrix_2 <- matrix(7:12, nrow = 3, ncol = 2, byrow = TRUE)

dim(matrix_1)
dim(matrix_2)
matrix_1 %*% matrix_2

