import random

# Write a function called is_even that takes a number as an argument 
# and returns True if it's even, and False otherwise

def is_even(num:int):
    '''
    :param num: int: number valuation
    :return: bool: 
    '''
    if num % 2 == 0:
        return True
    
    return False

gen_number:int = 10
random_list:list[int] = [round(random.uniform(1, 122)) for _ in range(gen_number)]

for num in random_list:
    print(num ,is_even(num))