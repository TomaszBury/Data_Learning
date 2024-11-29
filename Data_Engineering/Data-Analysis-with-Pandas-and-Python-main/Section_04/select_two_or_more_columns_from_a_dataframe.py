import pandas as pd
import secret as se

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# This challenge includes a "chicken_restaurants.csv" dataset with 6 columns:
# Name, Original Location, Year, Headquarters, Locations, Areas Served
# Import the CSV into a DataFrame and assign it to a "chicken" variable.

chicken = pd.read_csv(se.SECREAT + "chicken_restaurants.csv")


# Extract the "Year" and "Locations" columns (in that order) into
# their own DataFrame. Assign the DataFrame to a "years_and_locations" variable.

locations = ['Year', 'Locations']

years_and_locations = chicken[locations]

# Extract the "Locations", "Name", and "Headquarters" columns (in that order)
# into their own DataFrame. Assign the DataFrame to a
# "interesting_facts" variable.

locations = ['Locations', 'Name', 'Headquarters']

interesting_facts = chicken[locations]

# print(chicken)
# print(years_and_locations)
print(interesting_facts)
