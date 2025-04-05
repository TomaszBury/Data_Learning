number = 1
print(number)

print(class(number))

print(typeof(number))

my_date <- as.Date('2019-01-01')
print(class(my_date))
print(typeof(my_date))

word <- 'newspaper'
print(class(word))

logical_element <- FALSE
print(logical_element)

numeric_vector <- c(1.2, 3, 4)
print(class(numeric_vector))
numeric_vector <- c(1.2, 3, "4")
print(class(numeric_vector))

logical_element <- is.numeric(12)
print(logical_element)

logical_element <- is.numeric("12")
print(logical_element)

#Converting Data Types

number <- 23 
print(as.character(number))

print(is.numeric(as.numeric(as.character(number))))

numeric_vecotr <- c(1.2, 3, 4)
char_vector <- as.character(numeric_vector)
print(char_vector)
print(is.character(char_vector))
print(is.numeric(numeric_vecotr))

years_vector <- c(2001, 2002, 2003, "Not a Year")
print(as.character(years_vector))

# new_vector <- as.numeric(years_vector)
# print(new_vector)

logical_vector <- c(TRUE, FALSE, TRUE, FALSE, FALSE)
print(logical_vector)
print(as.numeric(logical_vector))

print(as.logical(as.numeric(logical_vector)))

labels <- c('Europe', 'Africa', 'Europe', 'North America', 'South America', 'Africa', 'Asia', 'Oceania', 'Antarctica')
print(labels)

factor_labels <- factor(labels)
print(factor_labels)
print(class(factor_labels))
print(typeof(factor_labels))

print(as.integer(factor_labels))

print(nlevels(factor_labels))

altitude_levels <- c('High', 'Low', 'Medium', 'Low', 'High', 'Low')
print(factor(altitude_levels))
print(nlevels(factor(altitude_levels)))

altitude_factor <- factor(altitude_levels, order=TRUE, levels=c('Low', 'Medium', 'High'))
print(factor_order)

print(as.integer(altitude_factor))

#Dealing with Dates

dates <- c('2019-01-01', '2019-01-02')
print(class(dates))
print(dates)

dates <- as.Date(c('2019-01-01', '2019-01-02'))
print(class(dates))
print(dates)

print(typeof(dates))
print(as.numeric(dates))

print(as.Date(c('01/01/2019')))
print(as.Date(c('01/01/2019'), format='%d/%m/%Y')) # y -> 99; Y -> 1999

example_date <- as.Date(c('01Jan2019'), format='%d%b%Y')
print(format(example_date, '%D'))
print(format(example_date, '%d'))
print(format(example_date, '%b'))
print(format(example_date, '%Y'))

print(format(dates, '%d'))
print(format(dates, '%D'))

days <- format(dates, '%d')
print(days)

print(class(10))
print(class(c(TRUE, FALSE)))
print(is.logical("TRUE"))