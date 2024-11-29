import pandas as pd
import secret as se

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# This challenge includes a cruise_ships.csv with 4 columns:
# Name, Operator, Year, and Tonnage
# Import the cruise_ships.csv DataFrame and assign it to
# a cruise_ships variable

cruise_ships = pd.read_csv(se.SECREAT + "cruise_ships.csv")

# Extract the "Operator" column from the DataFrame
# and assign it to an "operators" variable.

operators = cruise_ships['Operator']

# Extract the "Tonnage" column from the DataFrame
# and assign it to an "tonnages" variable.

tonnages = cruise_ships['Tonnage']

# Extract the "Name" column from the DataFrame
# and assign it to an "cruise_names" variable.

cruise_names = cruise_ships['Name']


# print(cruise_ships)
# print(operators)
# print(tonnages)
print(cruise_names)
