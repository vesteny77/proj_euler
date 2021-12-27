import doctest


def is_prime(n):
    pass


def find_primes_up_to(n=100):
    """
    Algorithm: Sieve of Eratosthenes
    Return a list of prime numbers up to and including n

    :param n: int
    :return: list

    >>> find_primes_up_to(2)
    [2]
    >>> find_primes_up_to(10)
    [2, 3, 5, 7]
    >>> find_primes_up_to(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    i, lim = 2, int(n ** 0.5)
    for i in range(i, lim + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]


def find_nth_prime(n):
    """
    Return the nth prime number. 2 is the 1st prime, 3 is the 2nd prime...

    :param n: int
    :return: int

    >>> find_nth_prime(1)
    2
    >>> find_nth_prime(6)
    13
    """
    bound = 2 * n
    primes = []
    while len(primes) < n:
        primes = find_primes_up_to(bound)
        bound += n
    return primes[n - 1]


if __name__ == "__main__":
    doctest.testmod()
    # print(find_primes_up_to(10))
