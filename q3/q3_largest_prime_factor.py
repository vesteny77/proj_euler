# What is the largest prime factor of the number 600851475143?

def prime_factors(n):
    """
    Return a list of prime factors of n
    :param n: int
    :return: list
    """
    # check if 2 is the largest prime
    all_factors = set()
    t = n
    while t % 2 == 0:
        t /= 2
        all_factors.add(2)

    # check the divisors greater than 2
    d = 3
    while d < n ** 0.5:
        while not t % d:
            t /= d
            all_factors.add(d)
        d += 2
    return all_factors


def largest_prime_factor(n):
    return max(prime_factors(n))


if __name__ == "__main__":
    print("The largest prime factor of the number 600851475143 is "
          f"{largest_prime_factor(600851475143)}")
