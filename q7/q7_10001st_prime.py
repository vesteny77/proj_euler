# What is the 10001st prime number?

import math_lib.prime as pr


def main():
    p = pr.find_nth_prime(10001)
    print(f"The 10,001st prime number is {p}")


if __name__ == "__main__":
    main()
