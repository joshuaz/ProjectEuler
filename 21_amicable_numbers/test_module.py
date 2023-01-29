import unittest
from amicable_numbers import sumAmicableNum
import math

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(sumAmicableNum(1000))
        expected = type(504)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = sumAmicableNum(1000)
        expected = 504
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = sumAmicableNum(2000)
        expected = 2898
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = sumAmicableNum(5000)
        expected = 8442
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test5(self):
        actual = sumAmicableNum(10000)
        expected = 31626
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()