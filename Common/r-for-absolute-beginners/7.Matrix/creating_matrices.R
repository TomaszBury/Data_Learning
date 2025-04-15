example_matrix <- matrix(data=1:4, nrow = 10, ncol = 4)
example_matrix

?matrix()

example_matrix <- matrix(data=1:4, nrow = 10, ncol = 4, byrow = TRUE)
example_matrix

example_matrix_2 <- array(data=1:4, dim = c(10,4))
example_matrix_2
example_matrix <- matrix(data=1:4, nrow = 10, ncol = 4)
example_matrix == example_matrix_2

class(example_matrix)
class(example_matrix_2)

dim(example_matrix)
ncol(example_matrix)
