import random

numbers:list[int] = [random.randint(1, 100) for _ in range(6)]

def find_max_number(numbers:list[int]) -> int:
    '''
    :param numbers: list[int]: list of integers
    :return: int - The maximum integer from the list.
    '''
    return max(numbers) if numbers else None

print(find_max_number(numbers=numbers))

