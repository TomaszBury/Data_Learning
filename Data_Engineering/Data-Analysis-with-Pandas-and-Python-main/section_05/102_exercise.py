import secret

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below
import pandas as pd

# This challenge includes a billboard.csv dataset.
# It is a list of the top-selling albums of all time according to Billboard
# The dataset has 5 columns:
# Artist,Album,Released,Genre,Sales
# Import the billboard.csv fille into a DataFrame.
# Assign the imported DataFrame to an 'billboard' variable.
billboard = pd.read_csv(secret.SECREAT + 'billboard.csv')

# CHALLENGE 1
# Find all records with an Artist of either Michael Jackson,
# Whitney Houston, or Celine Dion. Assign the resulting
# DataFrame to a "trios" DataFrame.
mask_artist = billboard['Artist'].isin(
    ['Whitney Houston', 'Celine Dion', 'Michael Jackson'])
trios = billboard[mask_artist]
# CHALLENGE 2
# Find all records with Sales of either 25, 35, or 45
# million copies. Note that the 'Sales' column's integers
# reflect album sales in millions. Assign the resulting DataFrame
# to a 'fives' DataFrame
mask_sales = billboard['Sales'].isin([25, 35, 45])
fives = billboard[mask_sales]
# CHALLENGE 3
# Find all records released in either 1979, 1989, or 1999.
# Assign the resulting DataFrame to a 'end_of_decade' DataFrame.
mask_released = billboard['Released'].isin([1979, 1989, 1999])
end_of_decade = billboard[mask_released]

print(end_of_decade)
