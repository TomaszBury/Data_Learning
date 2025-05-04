math_list  <- list(array(data = 1:2,dim = c(2,2,2)), c(3,9,81), matrix(c(9,0,9,0), nrow = 2, ncol = 2))

math_list

names(math_list) = c("ThreeDArray","Vector" , "Matrix")

math_list[[4]] <- "I DID IT !_!"

names(math_list) = c("ThreeDArray","Vector" , "Matrix",'String')

length(math_list)

math_list$String <- NULL

math_vector <- math_list[['Vector']]

math_vector <- array(math_vector)

str(math_vector)
typeof(math_vector)
class(math_vector)

new_matrix  <- math_list[['ThreeDArray']][2]

new_matrix <- new_matrix * math_vector[2]

new_matrix
