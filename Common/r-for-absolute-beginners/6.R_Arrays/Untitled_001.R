my_vector = 1:4

my_vector[1]

#my_vector[1,]

my_array = array(data = my_vector, dim = c(2, 2))

my_array[2,]

my_array[1,]

class(my_array)

class(my_vector)

my_array = array(data = my_vector, dim = c(2))

class(my_array)

my_array = array(data = my_vector, dim = c(2, 2, 2))

class(my_array)

typeof(my_array)

dim(my_array)



