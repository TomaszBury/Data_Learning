import pandas as pd
import secret as se

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# We have a hot_dogs.csv CSV file with 2 columns: Year and Winner.
# The dataset stores the winner of the world-famous Nathan's Hot Dog Eating
# contest for each year since 1967. You can explore the data by clicking into
# the CSV file on the left.
#
# Import the CSV file into a pandas Series object
# The Series should have the standard pandas numeric index
# The Series values should be the string values from the "Winner" column
# Assign the Series object to a "hot_dogs" variable

hot_dogs = pd.read_csv(se.SECREAT + "hot_dogs.csv",
                       usecols=["Winner"]).squeeze("columns")

# I'm curious how many times each winner has won the hot dog-eating contest.
# Create a new Series that shows each person's name (index labels)
# and the number of times they've won (the values). What method can
# help you generate this Series?
# Asssign the Series to a "names_and_wins" variable.

# names_and_wins = pd.Series(hot_dogs.value_counts())
names_and_wins = hot_dogs.value_counts()

# print(hot_dogs.value_counts().head())
print(names_and_wins.head())

#print(f"how many times each winner has won.:{hot_dogs.value_counts()}")
