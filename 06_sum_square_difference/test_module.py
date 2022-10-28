import unittest
from sum_square_difference import sum_square_difference
import math


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(sum_square_difference(10))
        expected = type(60)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = sum_square_difference(10)
        expected = 2640
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = sum_square_difference(20)
        expected = 41230
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = sum_square_difference(100)
        expected = 25164150
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()