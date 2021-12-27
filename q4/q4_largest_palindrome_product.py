# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(s: str):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def check_palindrome_recursive(s: str):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])
    return False


def __reverse_num(n: int):
    """
    Helper function for check_palindrome_num()

    Return a number with digits of n reversed.

    :param n: int
    :return: int
    """
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def check_palindrome_num(n: int):
    """
    Check whether n is a palindromic number without converting to a string
    :param n: int
    :return: bool
    """
    return __reverse_num(n) == n


def largest_palindrome_prod():
    lst = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if check_palindrome(str(i * j)):
                lst.append(i * j)
    return max(lst)


def largest_palindrome_prod_improved():
    """
    Improvement 1:
    The method above checks a * b and b * a. We can eliminate one of them
    by assuming that a <= b, roughly halving the number of iterations

    Improvement 2:
    Keep track of the current largest palindrome instead of storing them into
    a list and taking the maximum at the end

    Improvement 3: In the inner loop, if i * j is less than the current largest
    palindrome, then there's no need to check i * (j - 1), since it is guaranteed
    to also be less than the current largest palindrome.
    :return: int
    """
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            if i * j <= largest:
                break
            if check_palindrome_num(i * j): # i * j > largest
                largest = i * j
    return largest


def largest_palindrome_prod_improved_further():
    """
    After further analysis, we deduce that at least one of i or j must be
    a multiple of 11.

    See notes for more detailed explanation.

    :return: int
    """
    largest = 0
    i = 999
    while i >= 100:
        if i % 11 == 0:
            j = 999
            offset = 1
        else:
            # the largest number less than 999 and divisible by 11
            j = 990
            offset = 11
        while j >= i:
            if i * j <= largest:
                break
            if check_palindrome_num(i * j):
                largest = i * j
            j -= offset
        i -= 1
    return largest


if __name__ == "__main__":
    print("The largest palindrome made from the product of two 3-digit numbers is "
          f"{largest_palindrome_prod_improved_further()}")
