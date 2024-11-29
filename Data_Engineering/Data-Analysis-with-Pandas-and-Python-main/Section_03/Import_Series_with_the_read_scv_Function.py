# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

import pandas as pd

# We have a foods.csv CSV file with 3 columns: Item Number, Menu Item, Price
# You can explore the data by clicking into the foods.csv file on the left
# Import the CSV file into a pandas Series object
# The Series should have the standard pandas numeric index
# The Series values should be the string values from the "Menu Item" column
# Assign the Series object to a "foods" variable
foods = pd.read_csv(
    "C:\\Users\\Tom\\iCloudDrive\\Nauka\\Python\\Pyton_files\\Data-Analysis-with-Pandas-and-Python\\Section_03\\foods.csv", usecols=["Item"]).squeeze("columns")
print(foods)
