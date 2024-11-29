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
# Find all episodes that were EITHER in Season 4
# OR directed by Harold Ramis
# Assign the resulting DataFrame to a 'season_4_or_harold' variable.

mask_season = office['Season'] == 4
mask_directed = office['Director'] == 'Harold Ramis'

season_4_or_harold = office[mask_season | mask_directed]

# CHALLENGE 2:
# Find all episodes that EITHER had a Viewership less than 4
# OR aired on/after January 1st, 2013.
# Assign the resulting DataFrame to a 'low_viewership_or_later_airdate' variable.

mask_viewership = office['Viewership'] < 4
mask_airdate = office['Airdate'] >= '2013-01-01'

low_viewership_or_later_airdate = office[mask_viewership | mask_airdate]

# CHALLENGE 3:
# Find all episodes that EITHER the 9th episode of their season
# OR had an episode Name of "Niagara"
# Assign the resulting DataFrame to a 'ninth_or_niagara' variable.

mask_episode = office['Episode'] == 9
mask_name = office['Name'] == 'Niagara'

ninth_or_niagara = office[mask_episode | mask_name]

# print(office)
# print(season_4_or_harold)
# print(low_viewership_or_later_airdate)
print(ninth_or_niagara)
