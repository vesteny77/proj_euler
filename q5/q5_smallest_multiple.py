# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

import math
from math_lib.prime import find_primes_up_to


def gcd(a, b):
    if a >= b and a % b != 0:
        return gcd(b, a % b)
    elif a < b and b % a != 0:
        return gcd(a, b % a)
    else:
        return min(a, b)


def smallest_mult(n):
    lst_gcd_arg = []
    prod = math.factorial(n)
    for i in range(2, n + 1):
        lst_gcd_arg.append(prod // i)
    gcd_of_args = lst_gcd_arg[0]
    for i in range(len(lst_gcd_arg) - 1):
        gcd_of_args = gcd(gcd_of_args, lst_gcd_arg[i + 1])
    return prod // gcd_of_args


def smallest_mult2(n):
    primes_20 = find_primes_up_to(20)
    ret, lim = 1, n ** 0.5
    prime_exp = [0] * 20
    for p in primes_20:
        if p <= lim:
            prime_exp[p] = math.floor(math.log(n) / math.log(p))
        else:
            prime_exp[p] = 1
        ret *= p ** prime_exp[p]
    return ret


if __name__ == "__main__":
    print("The smallest positive number that is "
          "evenly divisible by all of the numbers from 1 to 20 is "
          f"{smallest_mult2(20)}")
