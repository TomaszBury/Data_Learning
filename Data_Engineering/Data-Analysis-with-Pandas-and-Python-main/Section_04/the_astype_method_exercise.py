import secret as se


# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Import the pandas library and assign it an alias of 'pd'.

import pandas as pd

# Import the health.csv file and assign it to a 'health' variable.
# The resulting DataFrame will have 3 columns: Weight, Height, and Blood Type
# Convert the values in the Weight Series to strings and overwrite the original column
# Convert the values in the Height Series to integers and overwrite the original column
# Convert the values in the Blood Type Series to categories and overwrite the original column

health = pd.read_csv(se.SECREAT + 'health.csv')

health['Weight'] = health['Weight'].astype(dtype='string')
health['Height'] = health['Height'].astype(dtype='int')
health['Blood Type'] = health['Blood Type'].astype(dtype='category')

print(health.info())
