# Find the sum of all the primes below two million.

from math_lib.prime import find_primes_up_to

L = 2000000


def sum_of_primes_up_to(lim):
    return sum(find_primes_up_to(lim))


if __name__ == "__main__":
    print(f"The sum of all the primes below two million is {sum_of_primes_up_to(L)}")