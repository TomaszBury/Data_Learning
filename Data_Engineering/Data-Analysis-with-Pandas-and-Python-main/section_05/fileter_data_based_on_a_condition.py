import secret

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below

import pandas as pd

# This challenge includes a the_office.csv dataset.
# It is a listing of all episodes in the popular American sitcom The Office.
# The dataset has 7 columns:
# Season, Episode, Name, Director, Writer, Airdate, Viewership
# Import the the_office.csv fille into a DataFrame.
# Tell pandas to parse the values in the Airdate column as datetime values.
# Finally, assign the imported DataFrame to an 'office' variable.

office = pd.read_csv(secret.SECREAT + 'the_office.csv',
                     parse_dates=['Airdate'])

# CHALLENGE 1:
# Find all episodes with a Writer of "Greg Daniels"
# Assign the resulting DataFrame to a 'written_by_greg' variable.

mask = office['Writer'] == 'Greg Daniels'

written_by_greg = office[mask]

# CHALLENGE 2:
# Find all episodes BEFORE season 8 (not including season 8)
# Assign the resulting DataFrame to a 'good_episodes' variable

mask = office['Season'] < 8

good_episodes = office[mask]

# CHALLENGE 3:
# Find all episodes that aired before 1/1/2008.
# Assign the resulting DataFrame to an 'early_episodes' variable.

mask = office['Airdate'] < '2008-01-01'

early_episodes = office[mask]

print(office)
print('\n\n\n\n')
print(written_by_greg)
print('\n\n\n\n')
print(good_episodes)
print('\n\n\n\n')
print(early_episodes)
