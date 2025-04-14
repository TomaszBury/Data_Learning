my_array_1 <- array(1:4, dim=c(2,2))

my_array_2 <- array(10:40, dim=c(2,2))

rbind(my_array_1, my_array_2)

dim(rbind(my_array_1, my_array_2))

cbind(my_array_1, my_array_2)

dim(cbind(my_array_1, my_array_2))


my_array_3 <- array(10:40, dim=c(2,3))
dim(cbind(my_array_1, my_array_3))

#dim(rbind(my_array_1, my_array_3))


array_1 <- array(c(1,5,20,20), dim=c(4,4))
array_2 <- array(c(1,5,20,20), dim=c(5,4))

cbind(array_1, array_2)
dim(rbind(array_1, array_2))
