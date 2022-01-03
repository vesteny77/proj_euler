# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from sympy.solvers import solve
from sympy import Symbol
import math


def is_int(x):
    return int(x) == x


def find_pythag_triplet():
    c = Symbol('c')
    a, b, soln = 0, 0, [0]
    for i in range(4):
        for j in range(4):
            a = 2 ** i * 5 ** j
            r = 1000 // a
            soln = solve(a ** 2 + (r * (500 - c)) ** 2 - c ** 2, c)
            if soln[0].is_Integer:
                b = r * (500 - int(soln[0]))
                break
    return a * b * soln[0], (a, b, soln[0])


def solve_test():
    x = Symbol('x')
    soln = solve(x + 1, x)
    print(soln[0].is_Integer)
    return


def find_pythag_triplet_optimized(s=1000):
    """
    Find the Pythagorean triplet (a, b, c) that satisfies a + b + c = s

    :param s: a + b + c
    :return: (a * b * c, (a, b, c))
    """
    s2 = s // 2
    lim = math.ceil(math.sqrt(s2)) - 1
    for m in range(2, lim + 1):
        if s2 % m == 0:
            s_m = s2 // m
            while s_m % 2 == 0:
                s_m //= 2
            k = m + 1
            if m % 2 == 1:
                k = m + 2
            while k < 2 * m and k <= s_m:
                if s_m % k == 0 and math.gcd(k, m) == 1:
                    d = s2 // (k * m)
                    n = k - m
                    a = d * (m ** 2 - n ** 2)
                    b = 2 * d * m * n
                    c = d * (m ** 2 + n ** 2)
                    return a * b * c, (a, b, c)
                k += 2
    return None


if __name__ == "__main__":
    ans = find_pythag_triplet_optimized()[0]
    a, b, c = find_pythag_triplet_optimized()[1]
    print(f"abc = {ans}")
    print(f"a = {a}, b = {b}, c = {c}")
    # solve_test()
