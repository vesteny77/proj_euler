# How many, not necessarily distinct, values of nCr
# for 1 ≤ n ≤ 100 are greater than one-million?

from math_lib.combinatorics import choose


def comb_greater_1m():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if choose(n, r) > 1000000:
                count += 1
    return count


if __name__ == "__main__":
    print(comb_greater_1m())
