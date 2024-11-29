# Calculate Sum of Digits
# Write a function called sum_of_digits that takes a positive integer as an argument and returns the sum of its digits.

def sum_of_digits(num: int) ->int:
    '''
    Function called sum_of_digits that takes a positive integer as an argument and returns the sum of its digits.

    :param num:int: - positive integer
    :return int: sum of its digits

    '''
    # num will be an integer
    result:int = 0
    
    for digit in str(num):
        result += int(digit)

    return result


assert sum_of_digits(11) == 2