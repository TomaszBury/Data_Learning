import random
# Find Unique Elements
# Find the number of unique elements of a 
# list: In: [1,3,4,5,6,7] Out: 6  In: [1,1,3,4,5,5,6,7] 
# Out: 6 (1 and 5 are duplicated and should be counted once)

def find_unique_elements(lst:list[int]) -> int:
    '''
    Finst number of unique elements.

    :param lst: list[int]: The input list containing integers.
    :return: int: number of qunique lemetns

    '''
    return len(set(lst))

out_first_test:int = 6
in_first_test:list[int] = [1,3,4,5,6,7]
assert find_unique_elements(in_first_test) == out_first_test