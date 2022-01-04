# Find the sum of the digits in the number 100!

from q16.q16_power_digit_sum import *
import math


def sum_of_digit_factorial(n):
    return sum_of_digits(math.factorial(n))


if __name__ == "__main__":
    print(sum_of_digit_factorial(100))
