vector = c(1,2,'3')

typeof(vector)

my_list = list(1, 2, '3')
my_list
typeof(my_list)

class(my_list)

multi_object <- list(
  c(1,2,3),
  array(1:4, dim=c(2,2)),
  TRUE
)

names(multi_object) = c('Vector', 'Array', 'Logiceal')

multi_object

length(multi_object)

str(multi_object)

multi_object_name <- list(
  'Vecktor' = c(1,2,3),
  'Array' = array(1:4, dim=c(2,2)),
  'logical' = TRUE
)

names(multi_object_name)
