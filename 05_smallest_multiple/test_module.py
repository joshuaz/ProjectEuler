import unittest
from smallest_multiple import smallest_multiple
import math


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(smallest_multiple(5))
        expected = type(60)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = smallest_multiple(5)
        expected = 60
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = smallest_multiple(7)
        expected = 420
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = smallest_multiple(10)
        expected = 2520
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test5(self):
        actual = smallest_multiple(13)
        expected = 360360
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()