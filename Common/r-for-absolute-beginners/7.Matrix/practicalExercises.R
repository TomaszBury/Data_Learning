fourdim <- array(1:10, dim = c(2,2,2,2))

fourdim[2,2,2,2]

fourdim[2,2,2,2] <- NA

fourdim[2,2,2,2]

median_value <- median(fourdim, na.rm = TRUE)

median_value

threed <- array(c(155, 261, 132000,423.4, 321, 137000,105, 240, 118000,157.64, 260, 139000), 
                dim = c(3,2,2), 
                dimnames = list(c('Stock Price','Revenue','Employees'), c('2018','2019'), c('Apple','Microsoft')))

threed

diff_price <- threed['Stock Price','2018','Apple'] - threed['Stock Price','2019','Apple']

diff_price

sum_price <- threed['Stock Price','2018','Apple'] + threed['Stock Price','2019','Apple']

sum_price

avg_price <- sum_price / 2

avg_price

procentage_difference <- (diff_price / avg_price) * 100
procentage_difference


apple <- threed[,,'Apple']
apple
 
stock_price <- threed['Stock Price',,]
stock_price

dim(stock_price)

class(stock_price) == class(threed)

stock_price[,'Microsoft']

price_vector <- as.vector(stock_price[,'Microsoft'])
price_vector
