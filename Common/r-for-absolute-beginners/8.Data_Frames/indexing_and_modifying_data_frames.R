countries_data <- data.frame(
  population= c(10280000, 66990000, 66650000),
  EU = c(TRUE, TRUE, FALSE),
  row.names = c('Portugal', 'France', 'UK')
)

countries_data[1,1]

countries_data[1,]

countries_data['France',]

countries_data[c('France','Portugal'),]

countries_data['Portugal','population']

countries_data['Portugal','population'] <- 1

countries_data['Portugal','population']
