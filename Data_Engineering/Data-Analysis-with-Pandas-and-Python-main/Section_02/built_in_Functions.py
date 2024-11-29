# Invoke the len function and pass it the string "Bobby"
# Assign the return value to a variable of name_length.
name_length = len("Bobby")


# Invoke the len function and pass it the string "Hollywood"
# Assign the return value to a variable of city_length.
city_length = len("Hollywood")


# Invoke the int function and pass it the string "31".
# Assign the return value to a variable of age_as_number.
age_as_number = int("31")



# Invoke the str function and pass it the number 31.
# Assign the return value to a variable of age_as_string.
age_as_string = str(31)


# CHALLENGE 
# Invoke the str function and pass it the number 99.
# The str function will return a string. Concatenate " problems" to the end of that string.
# Assign the final value to an "issues" variable.
# Thus, your "issues" variable should have a final value of "99 problems"
issues = str(99) + " problems"
print(f"{name_length}, {city_length}, {age_as_number}, {age_as_string}, {issues}")