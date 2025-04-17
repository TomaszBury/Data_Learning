countries_data <- data.frame(
  country = c('Portugal', 'France', 'UK'),
  population= c(10280000, 66990000, 66650000),
  EU = c(TRUE, TRUE, FALSE)
)

countries_data

spain_data <- data.frame(
  country = c('spain'),
  population = c(47280000),
  EU = c(TRUE)
)

str(spain_data)

str(countries_data)

rbind(countries_data, spain_data)

countries_data <- rbind(countries_data, spain_data)

countries_data

capitals <- c('Lisbon','Paris','London','Madrid')

cbind(countries_data, capitals)

countries_data <- cbind(countries_data, capitals)

countries_data[,'capitals']

str(countries_data)

countries_data[4,]

countries_data[-4,]

countries_data <- countries_data[-4,]

countries_data

countries_data[,'EU']

countries_data[,'EU'] <- NULL

countries_data

q4 <- data.frame(company=c("Amazon","Microsoft","Pfizer"), 
           stock_price= c(2000,150, 50),
           sector= c("Tech","Tech","Pharma"),
           tech= c(TRUE,TRUE,FALSE),
           stringsAsFactors = TRUE
)

str(q4)
