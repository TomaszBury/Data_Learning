import secret

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below
import pandas as pd

# This challenge includes a data.csv dataset.
# The dataset has 3 columns: Name, Title, Cryptocurrency
# Import the dataset and assign the DataFrame to a "data" variable.
data = pd.read_csv(secret.SECREAT + 'data.csv')

# Unfortunately, some of the text data has been incorrectly exported.

# The strings in the Name column are all lowercased.
# Capitalize the names properly (so the first letter of the person's first and last names are uppercase)
# Then, overwrite the Name column with the new Series.
data['Name'] = data['Name'].str.title()

# Lowercase the strings in the Title column.
# Then, overwrite the Title column with the new Series.
data['Title'] = data['Title'].str.lower()

# Uppercase the strings in the Cryptocurrency column.
# Then, overwrite the Cryptocurrency column with the new Series.

data['Cryptocurrency'] = data['Cryptocurrency'].str.upper()

print(data['Title'].str.lower())
