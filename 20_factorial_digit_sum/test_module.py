import unittest
from factorial_digit_sum import sumFactorialDigits
import math

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(sumFactorialDigits(10))
        expected = type(27)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = sumFactorialDigits(10)
        expected = 27
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = sumFactorialDigits(25)
        expected = 72
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = sumFactorialDigits(50)
        expected = 216
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test5(self):
        actual = sumFactorialDigits(75)
        expected = 432
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test6(self):
        actual = sumFactorialDigits(100)
        expected = 648
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()