import pandas as pd

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# Below, we have a list of delicious tortilla chip flavors
flavors = ["Spicy Sweet Chili", "Cool Ranch", "Nacho Cheese", "Salsa Verde"]

# Create a new Series object, passing in the flavors list defined above
# Assign it to a 'doritos' variable. The resulting Series should look like this:
#
#
#   0    Spicy Sweet Chili
#   1           Cool Ranch
#   2         Nacho Cheese
#   3          Salsa Verde
#   dtype: object

doritos = pd.Series(flavors)


# Below, sort the doritos Series in descending order.
# Assign the sorted a Series to a 'sorted_doritos' variable.
# The sorted Series should like this:
#
#   0    Spicy Sweet Chili
#   3          Salsa Verde
#   2         Nacho Cheese
#   1           Cool Ranch
#   dtype: object

sorted_doritos = doritos.sort_values(ascending=False)

print(f"{doritos}, {sorted_doritos}")
