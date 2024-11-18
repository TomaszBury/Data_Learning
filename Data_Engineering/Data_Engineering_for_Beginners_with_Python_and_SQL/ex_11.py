import math
from sympy import isprime
# Check for Prime Numbers
# Create a function called is_prime that takes an integer as input and 
# returns True if the number is prime and False otherwise. Your function should use only built-in Python tools.

def is_prime(number:int) -> bool:
    '''
    Function called is_prime that takes an integer as input and 
    returns True if the number is prime and False otherwise.
    
    :param number: int: integer to check if it is prime
    :returns bool: If number is prime
    '''
    # Your code here
    if number <= 1:
        return False
    
    i:int = 5 
    for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    return True


assert is_prime(5) == True
assert is_prime(17) == True
assert is_prime(4) == False
assert is_prime(1) == False
assert is_prime(9991) == isprime(9991)
