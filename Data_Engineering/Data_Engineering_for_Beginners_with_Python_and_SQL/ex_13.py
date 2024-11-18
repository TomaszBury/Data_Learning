# Calculate Average
# Write a Python program that calculates the average of a list of numbers.
# In:  [5, 10, 15, 20]
# Out:  12.5
# If the list is empty, return 0


def calculate_average(numbers:list[int]) -> float:
    '''
    Function that calculates the average of a list of numbers.

    :param numbers:list[int]: list to calculate average.
    :return float: average
    '''
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

assert calculate_average([5, 10, 15, 20]) == 12.5
assert calculate_average([]) == 0