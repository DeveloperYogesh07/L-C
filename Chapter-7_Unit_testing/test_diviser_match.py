import unittest
from io import StringIO
from unittest.mock import patch
from diviser_match import (
    count_total_divisors,
    count_adjacent_numbers_with_equal_divisors,
)


class TestDivisorSolution(unittest.TestCase):

    def test_count_total_divisors(self):
        """Test the function that counts total divisors of a number"""
        # Test cases with known divisor counts
        self.assertEqual(count_total_divisors(1), 1)
        self.assertEqual(count_total_divisors(6), 4)
        self.assertEqual(count_total_divisors(7), 2)
        self.assertEqual(count_total_divisors(12), 6)
        self.assertEqual(count_total_divisors(36), 9)

        # Test with a perfect square 
        self.assertEqual(count_total_divisors(9), 3)
        self.assertEqual(count_total_divisors(25), 3)

        # Test with a prime number
        self.assertEqual(count_total_divisors(17), 2)
        self.assertEqual(count_total_divisors(23), 2)

    def test_count_adjacent_numbers_with_equal_divisors(self):
        """Test counting pairs of consecutive integers with equal divisor counts"""
        self.assertEqual(count_adjacent_numbers_with_equal_divisors(3), 1)
        self.assertEqual(count_adjacent_numbers_with_equal_divisors(5), 1)
        self.assertEqual(count_adjacent_numbers_with_equal_divisors(10), 1)

        # Test edge cases
        self.assertEqual(count_adjacent_numbers_with_equal_divisors(2), 0)


if __name__ == "__main__":
    unittest.main()
