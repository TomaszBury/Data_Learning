import pandas as pd
import secret as se

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work


# We have a roller_coasters.csv CSV file with 4 columns: Name, Park, Country, and Height.
# You can explore the data by clicking into the CSV file on the left
# Import the CSV file into a pandas Series object
# The Series should have the standard pandas numeric index
# The Series values should be the string values from the "Name" column
# Assign the Series object to a "coasters" variable
coasters = pd.read_csv(se.SECREAT + "roller_coasters.csv",
                       usecols=["Name"]).squeeze("columns")


# I only want to ride the top 3 roller coasters on the list.
# Starting with the "coasters" Series, extract the first 3 rows in a new Series.
# Assign the new Series to a "top_three" variable.
top_three = coasters.head(3)


# I'm now curious about some of the last entries on the coaster list.
# Starting with the "coasters" Series, extract the last 4 rows in a new Series.
# Assign the new Series to a "bottom_four" variable.
bottom_four = coasters.tail(n=4)

print(f"{coasters}")
print(f"{top_three}")
print(f"{bottom_four}")
