# Find the sum of all the multiples of 3 or 5 below 1000.

def count_mult():
    s = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
                s += i
    return s


def count_mult2():
    # get the sum of multiples of 3 under 1000
    n_terms_3 = (999 - 3) // 3 + 1
    sum_mult_3 = (3 + 999) * n_terms_3 // 2

    # get the sum of multiples of 5 under 1000
    n_terms_5 = (995 - 5) // 5 + 1
    sum_mult_5 = (5 + 995) * n_terms_5 // 2

    # get the sum of multiples of 15 under 1000
    n_terms_15 = (990 - 15) // 15 + 1
    sum_mult_15 = (15 + 990) * n_terms_15 // 2

    # by the inclusion-exclusion principle
    return sum_mult_3 + sum_mult_5 - sum_mult_15


if __name__ == "__main__":
    print(f"The sum of all the multiples of 3 or 5 below 1000 is {count_mult2()}")
