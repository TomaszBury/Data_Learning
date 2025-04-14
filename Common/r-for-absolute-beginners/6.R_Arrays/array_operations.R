my_array <- array(data=c(100,100,100), dim = c(3,3,2))

# my_array

my_array[,,1] <- sqrt(my_array[,,1])

my_array[,,1]

my_array[,2,]

my_array[,2,] <- my_array[,2,]**2

my_array

my_array[,,1]*my_array[,,2]


my_array[1,3,2] <- my_array[1,3,2] / 5

my_array[1,3,2]
