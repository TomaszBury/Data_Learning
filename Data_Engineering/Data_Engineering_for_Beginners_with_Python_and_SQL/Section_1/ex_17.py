# Remove Duplicates from a List
# Create a function called remove_duplicates that takes a list of elements as input and returns a new list with duplicates removed. 
# Your function should use only built-in Python tools and should maintain the original order of elements while removing duplicates.

def remove_duplicates(input_list:list[int | str]) -> list[int | str]:
    # Your code here
    '''
    Function called remove_duplicates that takes a list of elements as input and returns a new list with duplicates removed.

    :param input_list: list[int | str]: 
    :return list[int | str]:    
    '''
    result_list:list[int | str] = []
    for var in input_list:
        if result_list.count(var) == 0:
            result_list.append(var)
    return result_list


assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates(['apple', 'banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []