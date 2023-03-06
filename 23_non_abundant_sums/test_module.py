import math
from non_abundant_sums import sumOfNonAbundantNumbers
import unittest

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(sumOfNonAbundantNumbers(10000))
        expected = 3731004
        self.assertEqual(type(actual), type(expected), 'Expected an int')

    def test2(self):
        actual = type(sumOfNonAbundantNumbers(10000))
        expected = 3731004
        self.assertEqual(actual, expected, 'Expected an int')

    def test3(self):
        actual = type(sumOfNonAbundantNumbers(15000))
        expected = 4039939
        self.assertEqual(actual, expected, 'Expected an int')

    def test4(self):
        actual = type(sumOfNonAbundantNumbers(20000))
        expected = 4159710
        self.assertEqual(actual, expected, 'Expected an int')

    def test5(self):
        actual = type(sumOfNonAbundantNumbers(28123))
        expected = 4179871
        self.assertEqual(actual, expected, 'Expected an int')
    

if __name__ == "__main__":
    unittest.main()
