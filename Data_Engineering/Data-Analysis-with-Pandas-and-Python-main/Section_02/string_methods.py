# Define a 'scientist' variable set to the string 'albert einstein'
# Invoke the title method on the string/variable
# Assign the returned string to a 'proper_name' variable
scientist = "albert einstein"
proper_name = scientist.title()

# The 'wasteful_string' below has a lot of useless whitespace
# Invoke the correct method on wasteful_string to clear ALL whitespace (beginning and end)
# Assign the returned string from the correct method to an 'unwasteful_string' variable
wasteful_string = "     9:00PM     "
unwasteful_string = wasteful_string.strip()

# The party_attendees string below contains a list of people attending our party
# Use the 'in' operator to determine if "Ron" is attending the party
# Assign the resulting Boolean to an 'is_attending' variable
party_attendees = "Sharon, James, Ron, Blake"
is_attending = "Ron" in party_attendees

# Declare a cleanup function that accepts a single string input
# The function should
#  1) remove all leading and trailing whitespace from the input string
#  2) capitalize the first letter of the input string
#  3) return the new string
# EXAMPLES:
# 
# cleanup("  hello  ")               => "Hello"
# cleanup("   see you tomorrow   ")  => "See you tomorrow"

def cleanup(input_string):
    return input_string.strip().capitalize()

print(f"{cleanup('   see you tomorrow   ')}, {proper_name}, {unwasteful_string}, {is_attending}")