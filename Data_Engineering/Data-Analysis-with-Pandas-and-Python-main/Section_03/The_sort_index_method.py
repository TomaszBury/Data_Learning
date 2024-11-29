# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd

# Below, we have a list of delicious drink flavors
# We create a sorted Series of strings and assign it to a 'gatorade' variable
flavors = ["Red", "Blue", "Green", "Orange"]
gatorade = pd.Series(flavors).sort_values()

# I'd like to return the Series to its original order
# (sorted by the numeric index in ascending order).
# Sort the gatorade Series by index.
# Assign the result to an 'original' variable.
print(f"{gatorade}")

original = gatorade.sort_index()

print(f"{original}")
