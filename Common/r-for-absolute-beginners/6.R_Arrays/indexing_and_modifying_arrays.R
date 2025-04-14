my_array = array(c(1:8), dim=c(4,4))

my_array

my_array[,4]

my_array[,3]

my_array[2:3,3]

my_array[1,]

my_array[,1] <- c(100,100,100,100)

my_array

my_array[1:2,] <- array(c(1000,1000,1000,1000,1000,1000,1000,1000), dim = c(2,4))

my_array
