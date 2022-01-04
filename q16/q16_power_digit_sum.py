# What is the sum of the digits of the number 2^1000?

def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


if __name__ == "__main__":
    print(f"The sum of the digits of the number 2^1000 is {sum_of_digits(2 ** 1000)}.")
