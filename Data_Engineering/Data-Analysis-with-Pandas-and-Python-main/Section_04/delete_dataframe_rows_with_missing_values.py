import pandas as pd
import secret as se

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# The data.csv file contains a dataset of random numbers.
# The dataset has 4 columns: A, B, C, and D.
# Import pandas and use it to parse the CSV.
# Assign the imported DataFrame to a variable called 'data'.

data = pd.read_csv(se.SECREAT + 'data.csv')

# Filter the dataset to remove rows where ALL the
# values are missing. Assign the resulting DataFrame
# to a "no_empty_rows" variable.

no_empty_rows = data.dropna(how='all')

# Filter the dataset to remove rows that have a missing value
# in either the "B" or "D" columns.
# Assign the resulting DataFrame to a "result" variable.

check_columns = ['B', 'D']
result = data.dropna(subset=check_columns)

print(data)
print('\n')
# print(no_empty_rows)
print(result)
