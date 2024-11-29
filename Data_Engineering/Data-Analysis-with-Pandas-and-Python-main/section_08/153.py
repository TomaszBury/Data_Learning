import os
import pandas as pd

cwd = os.getcwd() + '\\section_08\\'

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below

# This challenge includes a weather.csv dataset.
# It is a listing of temperatures across 4 seasons in several cities
# The dataset has 4 columns: City,Fall,Winter,Spring,Summer
# Notice that the Fall, Winter, Spring, and Summer columns are storing
# the same data point -- the temperature. This makes them good candidates
# for melting into a single column.
# Import the weather.csv file into a DataFrame.
# Assign the imported DataFrame to a 'weather' variable.

weather = pd.read_csv(cwd + 'wether.csv')

# CHALLENGE 1:
# Create a new DataFrame using the 'weather' DataFrame by 'melting'
# the season columns' values into a single one. The 4 Season values
# should be stored in a column called 'Season'. The temperature
# values should be stored in a column called 'Temperature'.
# Your goal is a DataFrame that looks like this:
#
# City	    Season	 Temperature
# London	Fall	 68
# London	Winter	 94
# London	Spring	 103
# London	Summer	 21
# Paris	    Fall	 46
# Paris	    Winter	 86
# Paris	    Spring	 26
# Paris	    Summer	 70
# ... more rows
#
# Assign this DataFrame to a 'melted' variable

melted = pd.melt(weather, id_vars='City', var_name='Season',
                 value_name='Temperature')

print(melted)
