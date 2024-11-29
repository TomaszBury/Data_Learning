import secret
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# Let's start by importing pandas below
import pandas as pd

# This challenge includes a weather.csv dataset. It includes
# temperature measurements (high and low) for the month of April.
# The dataset has 3 columns:
# Day, Low Temp, High Temp
# Import the weather.csv file into a DataFrame.
# Tell pandas to parse the values in the Day column as datetime values.
# Finally, assign the imported DataFrame to a 'weather' variable.
weather = pd.read_csv(secret.SECREAT + 'weather.csv', parse_dates=['Day'])

# CHALLENGE 1
# I want to see the temperature for the days between April 15, 2022 and April 22, 2022.
# Extract those rows to a new DataFrame and assign it to a 'week_of_weather' variable
mask_day = weather['Day'].between('2022-04-15', '2022-04-22')
week_of_weather = weather[mask_day]
# CHALLENGE 2
# Extract the rows where the value in the Low Temp column is between 30 and 50.
# Assign the new DataFrame to a "cold_days" variable.
mask_temp = weather['Low Temp'].between(30, 50)
cold_days = weather[mask_temp]
# CHALLENGE 3
# Extract the rows where the value in the High Temp column is between 50 and 75.
# Assign the new DataFrame to a "warm_days" variable.
mask_temp = weather['High Temp'].between(50, 75)
warm_days = weather[mask_temp]


# print(weather)
# print(week_of_weather)
# print(cold_days)
print(warm_days)
