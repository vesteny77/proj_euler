# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from sympy.solvers import solve
from sympy import Symbol


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


if __name__ == "__main__":
    ans = find_pythag_triplet()[0]
    a, b, c = find_pythag_triplet()[1]
    print(f"abc = {ans}")
    print(f"a = {a}, b = {b}, c = {c}")
    # solve_test()
