# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
from locale import currency


def easy_money():
    return 100


# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    return "Sushi"



# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"
def convert_to_currency(amount):
    return "$" + str(amount)

print(f"{convert_to_currency(15)}, {easy_money()}, {best_food_ever()}")