countries_data <- data.frame(
  country = c('Portugal', 'France', 'UK'),
  population= c(10280000, 66990000, 66650000),
  EU = c(TRUE, TRUE, FALSE)
)

#structure 
str(countries_data)

class(countries_data)

typeof(countries_data)

countries_data <- data.frame(
  population= c(10280000, 66990000, 66650000),
  EU = c(TRUE, TRUE, FALSE),
  row.names = c('Portugal', 'France', 'UK')
)

str(countries_data)
