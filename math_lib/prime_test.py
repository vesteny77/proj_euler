import unittest
from prime import *


class PrimeTest(unittest.TestCase):
    def test_find_primes_up_to(self):
        expected = [2, 3, 5, 7, 11,
                    13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71,
                    73, 79, 83, 89, 97]
        actual = find_primes_up_to()
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_nth_prime(self):
        self.assertEqual(97, find_nth_prime(25))

    def test_is_prime(self):
        pass


if __name__ == '__main__':
    unittest.main()
