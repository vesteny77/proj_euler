# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import math_lib.combinatorics as comb


def main():
    # number of lattice paths from (0, 20) to (20, 0)
    # this is equivalent to the number of lattice paths
    # from (0, 0) to (20, 20)
    print(f"The # of such routes through a 20 x 20 grid is {comb.choose(40, 20)}")


if __name__ == "__main__":
    main()
