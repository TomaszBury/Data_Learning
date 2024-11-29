import pandas as pd

# I have a dictionary that maps guitar types to their colors
guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

# Create a new Series object, passing in the guitars_dict dictionary as the data source.
# Assign the resulting Series to a "guitars" variable.
guitars = pd.Series(guitars_dict)

# Access the value for the index position of 0 within the "guitars" Series.
# Assign the value to a "fender_color" variable.

fender_color = guitars[0]

# Access the value for the index label of "Gibson Les Paul" in the "guitars" Series.
# Assign the value to a "gibson_color" variable.

gibson_color = guitars["Gibson Les Paul"]

# Access the value for the index label of "ESP Eclipse" in the "guitars" Series.
# Assign the value to a "esp_color" variable.

esp_color = guitars["ESP Eclipse"]

print(
    f"fender_color:{fender_color}; gibson_color:{gibson_color}; esp_color:{esp_color}")
