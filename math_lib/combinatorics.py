import math
import doctest


def pick(n, k):
    """
    Return the number of ways to select k objects from n objects with order
    :param n: int
    :param k: int
    :return: int
    >>> pick(1, 0)
    1
    >>> pick(1, 2)
    0
    >>> pick(5, 2)
    20
    """
    return math.factorial(n) // math.factorial(n - k) if n >= k else 0


def choose(n, k):
    """
    Return the number of ways to select k objects from n objects without order
    :param n: int
    :param k: int
    :return: int
    >>> choose(1, 0)
    1
    >>> choose(1, 2)
    0
    >>> choose(5, 2)
    10
    """
    return pick(n, k) // math.factorial(k) if n >= k else 0


if __name__ == "__main__":
    doctest.testmod()
