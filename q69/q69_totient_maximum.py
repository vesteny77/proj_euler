# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n
# which are relatively prime to n.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

import math


def totient(n):
    ret = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            ret += 1
    return ret


def n_over_totient(n):
    return n / totient(n)


def main():
    ret = 1
    some_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for p in some_primes:
        t = ret * p
        if t <= 1000000:
            ret = t
        else:
            break
    ratio_max = n_over_totient(ret)
    print(f"The max value of n ≤ 1,000,000 s.t. n/φ(n) is {ret} with ratio = {ratio_max}.")
    return ret


if __name__ == "__main__":
    main()
    # print(n_prime_factors(7))
