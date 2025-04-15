matrix_example <- matrix(c(100,23,42,23,342,203),nrow = 3, ncol = 2)
matrix_example

one_matrix <- matrix_example / matrix_example
one_matrix

one_matrix[,1] <- log(matrix_example[,1])
one_matrix

one_matrix[2,] <- one_matrix[2,] * 0.33
one_matrix

one_matrix_t <- t(one_matrix)
one_matrix_t

dim(matrix_example)
dim(one_matrix_t)

matrix_mul <- matrix_example %*% one_matrix_t
matrix_mul
