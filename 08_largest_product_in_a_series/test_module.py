import unittest
import math
from largest_product_in_a_series import largest_product_in_a_series


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(largest_product_in_a_series(4))
        expected = type(4)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = largest_product_in_a_series(4)
        expected = 5832
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test2(self):
        actual = largest_product_in_a_series(13)
        expected = 23514624000
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
if __name__ == "__main__":
    unittest.main()