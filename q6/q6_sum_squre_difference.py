# Find the difference between the sum of the squares of
# the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2


def sum_sq_diff(n):
    return abs(square_of_sum(n) - sum_of_squares(n))


if __name__ == "__main__":
    print("The difference between the sum of the squares of "
          "the first one hundred natural numbers and the square of the sum is "
          f"{sum_sq_diff(100)}")