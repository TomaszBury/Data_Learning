import pandas as pd
import os
cwd = os.getcwd() + '\\section_08\\'

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below

# This challenge includes a subway_locations.csv dataset.
# It is a listing of all US locations of the Subway fast food restaurant chain.
# The dataset has 4 columns:
# city,state,latitude,longitude

# CHALLENGE 1:
# Import the subway_locations.csv file into a DataFrame.
# Create a MultiIndex with the levels coming from the 'state' and 'city' columns (in that order)
# Sort the index (all columns must be sorted) and assign the resulting DataFrame to a 'subway' variable.

subway = pd.read_csv(cwd + 'subway_locations.csv', index_col=['state', 'city'])
subway = subway.sort_index()

# CHALLENGE 2:
# Using your DataFrame, access the Index holding the values from
# the 'city' level. Assign the Index to a `city_index` variable.

city_index = subway.index.get_level_values('city')

# CHALLENGE 3:
# Using your DataFrame, access the Index holding the values from
# the 'state' level. Assign the Index to a `state_index` variable.

state_index = subway.index.get_level_values('state')

print(state_index)
