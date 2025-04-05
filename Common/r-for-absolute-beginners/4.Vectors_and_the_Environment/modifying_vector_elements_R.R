melons <- c(1.2, 1.4, 2.4, 3.4)

melons[1] <-2 

melons[2:4] <- c(3,4,5)

melons[5] <- 10

new_melons <- c(1.2, 1.4, 2.4, 3.4, 1.2)

new_melons[new_melons<2] <- 2

new_new_melons <- melons[-c(2,4)]

vector_a <- c(1,2,3,4,5)

mean(vector_a)

max(vector_a)

var(vector_a)

vector_discount <- c(0.2, 0.2, 0.1, 0.05, 0.05)

vector_a * (1-vector_discount)

c(1, 3, 5) + c(1 ,2)

c(1, 4, 5, 6) + c(2, 4, 5, 5)

c(2,3,4,4,5) > 4
