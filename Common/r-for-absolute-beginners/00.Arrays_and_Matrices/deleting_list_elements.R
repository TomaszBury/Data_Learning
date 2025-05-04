example_list <- list(c('a','b','c'), array(1:10, dim=c(2,5)))

example_list[[3]] <- c(19:57)

example_list

example_list[[3]] <- NULL

example_list

example_list[[3]] <- c(1:7)

example_list

example_list[3] <- NULL

example_list

example_list[[3]] <- c(1:7)

names(example_list) <- c('List','Array', 'Funny_busines')

str(example_list)

example_list$Funny_busines <- NULL

example_list

