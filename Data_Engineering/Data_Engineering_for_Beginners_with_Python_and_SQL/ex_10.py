# Find the Nth Fibonacci Number
# Create a function called find_fibonacci that takes a non-negative integer n as input and 
# returns the n-th Fibonacci number. 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
# usually starting with 0 and 1. Your function should use only built-in Python tools.

def find_fibonacci(n:int) -> int:
    '''
    function called find_fibonacci that takes a non-negative integer n as input and returns the n-th Fibonacci number. 

    :param n: int: - non-negative integer
    :returns int: n-th Fibonacci number
    
    '''
    # Your code here
    fib_series:list[int] = [0,1]
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n > 1:
        for _ in range(n-1):
            fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[-1]

assert find_fibonacci(0) == 0
assert find_fibonacci(1) == 1
assert find_fibonacci(5) == 5
assert find_fibonacci(10) == 55