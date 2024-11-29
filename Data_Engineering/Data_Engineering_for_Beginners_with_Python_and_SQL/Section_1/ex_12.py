# Count Primes
# Description: Write a function that takes an integer n as input and returns the count of prime numbers less than n. 
# Input: 10 Output: 4 (Primes less than 10: 2, 3, 5, 7)
def count_primes(n:int) -> list[int]:
    '''
    Function that takes an integer n as input and returns the count of prime numbers less than n.

    :param n: int: prime numbers less than n
    :return list[int]: returns the count of prime numbers less than n
    '''
    # your code here
    if n <= 2:
        return 0
    
    prime = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is still true, then it is a prime
        if prime[p] == True:
            # Update all multiples of p to false, starting from p * p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    # Collecting all prime numbers
    prime_numbers = [p for p in range(2, n + 1) if prime[p]]
    return len(prime_numbers)

assert count_primes(10) == 4
assert count_primes(2) == 0