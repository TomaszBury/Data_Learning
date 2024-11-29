import pandas as pd
import os
cwd = os.getcwd() + '\\section_08\\'

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# This challenge includes a subway_locations.csv dataset.
# It is a listing of all US locations of the Subway fast food restaurant chain.
# The dataset has 4 columns:
# city,state,latitude,longitude

# CHALLENGE 1:
# Import the subway_locations.csv file into a DataFrame.
# Use the 'index_col' parameter to attach a MultiIndex with levels
# coming from the 'state' and 'city' columns (in that order)
# Sort the DataFrame by both index levels (in regular ascending order)
# Assign the resulting DataFrame to a 'subway' variable.

subway = pd.read_csv(cwd + 'subway_locations.csv', index_col=[
                     'state', 'city']).sort_index()

# CHALLENGE 2:
# Extract the row(s) with a 'state' level value of 'OK' and a
# 'city' level value of 'Broken Arrow'. Assign the result to a
# 'broken_arrow' variable.

broken_arrow = subway.loc[('OK', 'Broken Arrow')]

# CHALLENGE 3:
# Extract the row(s) with a 'state' level value of 'FL' and a
# 'city' level value of 'Winter Park'. Assign the result to a
# 'winter_park' variable.

winter_park = subway.loc[('FL', 'Winter Park')]

print(winter_park)
