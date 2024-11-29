# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# The code below defines a list of delicious foods
# and some dipping sauces to dip them in

from dataclasses import dataclass
import pandas as pd

foods = ["French Fries", "Chicken Nuggets", "Celery", "Carrots"]
dipping_sauces = ["BBQ", "Honey Mustard", "Ranch", "Sriracha"]

# Create a Series and assign it to the s1 variable below.
# Assign the foods list as the data source
# and the dipping_sauces list as the Series index
# For this solution, use positional arguments (i.e. feed in the arguments sequentially)
s1 = pd.Series(foods, dipping_sauces)


# Create a Series and assign it to the s2 variable below.
# Assign the dipping_sauces list as the data source
# and the foods list as the Series index
# For this solution, use keyword arguments (i.e. provide the parameter names
# alongside the arguments)
s2 = pd.Series(index=foods, data=dipping_sauces)
