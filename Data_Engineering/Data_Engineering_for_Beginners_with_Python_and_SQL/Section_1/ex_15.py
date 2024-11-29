# Find the Missing Number
# Create a function called find_missing_number that takes a list of distinct integers from 0 to n (inclusive), 
# where n is one less than the length of the list, and returns the missing number from the list. 
# Your function should use only built-in Python tools.


def find_missing_number(nums:list[int]) -> int:
    '''
    Function called find_missing_number that takes a list of distinct integers from 0 to n (inclusive), 
    where n is one less than the length of the list, and returns the missing number from the list. 
    
    :param nums: list[int]:
    :return int:
    '''
    
    for num in range(len(nums) + 1):
        if nums.count(num) == 0:
            return num
    return 0

assert find_missing_number([0, 1, 3]) == 2
assert find_missing_number([4, 1, 3, 2, 0, 6, 7, 5]) == 8
assert find_missing_number([9, 7, 2, 1, 0, 6, 8, 4, 5, 3]) == 10
assert find_missing_number([]) == 0