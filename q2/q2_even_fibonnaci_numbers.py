# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.

import numpy as np
import math


def naive_fib(n):
    # recursion
    if n == 1 or n == 2:
        return 1
    else:
        return naive_fib(n - 1) + naive_fib(n - 2)


def dp_fib(n):
    """
    Return the nth Fibonacci number
    :param n: int
    :return: int
    """
    memo = [0 for _ in range(n + 1)]
    memo[1], memo[2] = 1, 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def mat_fib(n):
    # divide and conquer
    base = np.array([[1, 1], [1, 0]])
    ret = base
    for _ in range(n):
        ret = base @ ret
    print(ret)
    return ret[1][1]


def closed_form_fib(n):
    return int((1 / math.sqrt(5)) * ((1 + math.sqrt(5)) / 2) ** n -
               (1 / math.sqrt(5)) * ((1 - math.sqrt(5)) / 2) ** n)


def closed_form_even_fib(n):
    return int((5 + 2 * math.sqrt(5)) / 5 * (2 + math.sqrt(5)) ** n +
               (5 - 2 * math.sqrt(5)) / 5 * (2 - math.sqrt(5)) ** n)


def print_fib(n):
    memo = [0 for _ in range(n + 1)]
    memo[1], memo[2] = 1, 1
    print(memo[1], memo[2], end=" ")
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
        print(memo[i], end=" ")
    print()


def print_even_fib(n):
    memo = [0 for _ in range(n + 1)]
    memo[1], memo[2] = 1, 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
        if memo[i] % 2 == 0:
            print(memo[i], end=" ")
    print()


def find_even_fib_sum():
    base = np.array([[1, 1], [1, 0]])
    tmp = base
    ret = 0
    while tmp[1][1] < 4000000:
        tmp = base @ tmp
        if tmp[1][1] % 2 == 0:
            ret += tmp[1][1]
    return ret


def find_even_fib_sum2():
    i, ret = 0, 0
    while closed_form_even_fib(i) < 4000000:
        ret += closed_form_even_fib(i)
        i += 1
    return ret


if __name__ == "__main__":
    print(f"The sum of even Fibonacci numbers under 4 million is {find_even_fib_sum2()}")
