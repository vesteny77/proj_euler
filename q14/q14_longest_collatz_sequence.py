# Which starting number, under one million,
# produces the longest chain of Collatz sequence?

LIM = 1000000


def longest_collatz():
    """
    Return (m, n) where m is the length of the longest chain and
    n is the starting number that produces m

    :return: 2-tuple
    """
    m, n = 0, 0
    for i in range(LIM):
        count, t = 0, i
        while t > 1:
            if t % 2 == 0:
                t //= 2
            else:
                t = 3 * t + 1
            count += 1
        count += 1
        if count > m:
            m, n = count, i
    return m, n


if __name__ == "__main__":
    print(f"The starting number that "
          f"produces the longest chain under one million is {longest_collatz()}.")