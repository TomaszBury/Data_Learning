import pandas as pd
import os
cwd = os.getcwd() + '\\' + 'section_08\\'


# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below

# This challenge includes a subway_locations.csv dataset.
# It is a listing of all US locations of the Subway fast food restaurant chain.
# The dataset has 4 columns:
# city,state,latitude,longitude
# Import the subway_locations.csv file into a DataFrame.
# Assign the imported DataFrame to a 'subway' variable.
subway = pd.read_csv(cwd + 'subway_locations.csv')

# CHALLENGE 1:
# Create a MultiIndex with the levels coming from the 'state' and 'city' columns (in that order)
# Assign the resulting DataFrame to a 'multi_df' variable.
# Do not mutate the original DataFrame.
multi_df = subway.set_index(keys=['state', 'city'])

# CHALLENGE 2:
# Using your MultiIndex DataFrame, sort the index by both levels' values
# Assign the resulting DataFrame to a 'sorted_multi_df' variable.
# Do not mutate any previous DataFrames.
sorted_myulti_df = multi_df.sort_index()

print(multi_df)
print(sorted_myulti_df)
# print(cwd)
