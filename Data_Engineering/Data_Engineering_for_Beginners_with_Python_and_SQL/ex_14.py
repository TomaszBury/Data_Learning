# Count Occurrences in a List
# Write a Python function that takes a list of numbers and a target number, 
# and it returns the count of how many times the target number appears in the list.

# In: ([1, 2, 3, 4, 2, 2, 5], 2)
# Out: 3

def count_occurrences(numbers:list[int], target:int) -> int:
    '''
    function that takes a list of numbers and a target number, 
    and it returns the count of how many times the target number appears in the list.

    :param numbers: list[int]: list of numbers
    :returns int: target number appears in the list.
    '''
    return numbers.count(target)

assert count_occurrences([1, 2, 3, 4, 2, 2, 5],2) == 3