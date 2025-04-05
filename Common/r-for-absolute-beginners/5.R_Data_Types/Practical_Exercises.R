boolean_vec <- c(rep(TRUE, 5), rep(FALSE, 3))

print(boolean_vec==c(TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE))

numeric_vec <- as.numeric(boolean_vec)
print(numeric_vec)

print(is.numeric(numeric_vec))

char_vec <- as.character(numeric_vec)
print(class(char_vec))

numeric_vec[5] ="5"
print(numeric_vec[5])

print(class(numeric_vec))

print(class(numeric_vec) == class(char_vec))