# Find Common Elements in Two Lists
# Create a function called find_common_elements that takes two lists of integers as input and returns a 
# list containing the common elements between the two input lists. The order of elements in the resulting list does not matter. 
# Your function should use only built-in Python tools.

def find_common_elements(list1:list[int], list2:list[int]) -> list[int]:
    '''
    Function called find_common_elements that takes two lists of integers as input and returns a 
    list containing the common elements between the two input lists.

    :param list1: list[int]:
    :param list2: list[int]:
    :return list[int]:
    
    '''
    # Your code here
    return list(set(list1) & set(list2))


assert find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]
assert find_common_elements([10, 20, 30], [30, 40, 50]) == [30]
assert find_common_elements([1, 2, 3], [4, 5, 6]) == []
assert find_common_elements([], [1, 2, 3]) == []