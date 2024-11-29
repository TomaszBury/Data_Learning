# Import the pandas library and assign it its "pd" alias

import pandas as pd

# Create a list with 4 countries - United States, France, Germany, Italy
countries_list = ["United States", "France", "Germany", "Italy"]
# Create a new Series by passing in the list of countries
countries = pd.Series(countries_list)
# Assign the Series to a "countries" variable


# Create a list with 3 colors - red, green, blue
# Create a new Series by passing in the list of colors
# Assign the Series to a "colors" variable
colors_list = ["red", "green", "blue"]
colors = pd.Series(colors_list)


# Given the "recipe" dictionary below,
# create a new Series by passing in the dictionary as the data source
# Assign the resulting Series to a "series_dict" variable
recipe = {
    "Flour": True,
    "Sugar": True,
    "Salt": False
}

series_dict = pd.Series(recipe)

print(f"{colors}")
print(f"{countries}")
print(f"{series_dict}")
