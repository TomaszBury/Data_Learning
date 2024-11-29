# Fibonacci Series
# Write a program that generates the Fibonacci series up to a given number 'n'.
# fibonacci(0) -> []
# fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
# fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n:int) -> list[int]:
    '''
    Function that generates the Fibonacci series up to a given number 'n'.

    :param n: int: how long sequence n > 2
    :return linst[int]: fibonacci series
    '''
    fib_series:list[int] = []
    next_fib_in_seq:int = 0
    if n == 0:
        return fib_series
    
    if n == 1:
        return fib_series.append(next_fib_in_seq)

    
    if n > 2:
        fib_series.append(next_fib_in_seq)
        fib_series.append(1)
        for _ in range(n):
            next_fib_in_seq = fib_series[-1] + fib_series[-2]
            if n >= next_fib_in_seq:
                fib_series.append(next_fib_in_seq)
            else:
                break
    # your code here
    print(f"n:{n} fib:{fib_series}")
    return fib_series


assert fibonacci(0) == []
assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
assert fibonacci(23) == [0, 1, 1, 2, 3, 5, 8, 13, 21]