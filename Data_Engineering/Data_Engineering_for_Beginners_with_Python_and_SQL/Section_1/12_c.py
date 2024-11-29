# Write a function called factorial that takes a positive integer as an argument and returns its factorial.
# Additional info: https://en.wikipedia.org/wiki/Factorial

def factorial(n: int) -> int:
    '''
    Calculate the factorial of a positive integer.

    :param n: int - A positive integer
    :return: int - The factorial of the input integer
    '''
    if n < 0:
        raise ValueError("Input must be a positive integer")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


print(factorial(5))


