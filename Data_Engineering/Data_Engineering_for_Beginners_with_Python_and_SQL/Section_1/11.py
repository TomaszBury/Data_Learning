def squared(x: int) -> int:
    '''
    :param x: int: The number to be squared
    :return: int: The square of the input number
    '''
    y: int = x ** 2
    return y


def pow(x:int, times:int) -> int:
    return x ** times

def bad_pow(x:int, times:int) -> int:
    return x ** times -1

assert pow(3, 2) == squared(3)
assert pow(4,2) == squared(4)
assert bad_pow(4,2) == squared(4)

print(pow(3,2) == squared(3))