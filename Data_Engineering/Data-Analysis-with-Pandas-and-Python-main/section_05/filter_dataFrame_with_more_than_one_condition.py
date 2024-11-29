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
# Import the the_office.csv file into a DataFrame.
# Tell pandas to parse the values in the Airdate column as datetime values.
# Finally, assign the imported DataFrame to an 'office' variable.

office = pd.read_csv(secret.SECREAT + 'the_office.csv',
                     parse_dates=['Airdate'])

# CHALLENGE 1:
# Find all episodes with a Viewership greater than 10
# who are also directed by Jeffrey Blitz
# Assign the resulting DataFrame to a 'jeffs_episodes' variable.

mask_views = office['Viewership'] > 10
mask_director = office['Director'] == 'Jeffrey Blitz'

jeffs_episodes = office[mask_views & mask_director]

# CHALLENGE 2:
# Find all episodes in season 5 that have an episode number
# greater than or equal to 13.
# Assign the resulting DataFrame to a "second_half_of_season_5" variable.

mask_season = office['Season'] == 5
mask_episode = office['Episode'] >= 13
second_half_of_season_5 = office[mask_season & mask_episode]

# CHALLENGE 3:
# Find all episodes that were the 6th episode of their season
# and also aired before 01/01/2010.
# Assign the resulting DataFrame to a "sixth_episodes_of_early_seasons" variable.

mask_episode = office['Episode'] == 6
mask_airdate = office['Airdate'] < '2010-01-01'
sixth_episodes_of_early_seasons = office[mask_episode & mask_airdate]

# print(jeffs_episodes)
# print(second_half_of_season_5)
print(sixth_episodes_of_early_seasons)
