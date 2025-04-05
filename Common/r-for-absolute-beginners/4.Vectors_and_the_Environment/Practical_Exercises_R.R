kids_ages <- c(12, 11, 12, 13, 14, 13, 12, 10, 12, 12, 14, 13)

mean(kids_ages)

sum(kids_ages)

subset_ages <- which(kids_ages >13)

names(kids_ages) <- c("John", "Rachel", "Joe", "Anne", "Theresa", "Samuel", "Marcus", "Andrew", "Kate", "Jane", "Martha", "David")

print(kids_ages)

subset_ages <- kids_ages[which(names(kids_ages) == "Rachel" | names(kids_ages) == "Anne")]

print(subset_ages)

print(kids_ages[5] <- 13)

under_12 <- which(kids_ages < 12)

print(under_12)


product_pricing <- c(5.6, 11.2, 4.5, 0.25, 1, 23)

half_price <- product_pricing / 2

print(half_price)

promotions_procent <- c(0.2, 0, 0.4, 0, 0.5, 0)

promotion <- product_pricing * (1 - promotions_procent)

print(product_pricing)
print(promotion)

squared_prices <- sqrt(product_pricing)
print(squared_prices)

first_three <- product_pricing[1:3]

maximum_price <- max(product_pricing)

print(maximum_price)


num_products <- length(product_pricing)
print(num_products)

transform_price <- sum(product_pricing)
print(transform_price)