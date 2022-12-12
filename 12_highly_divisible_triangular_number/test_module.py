import unittest
from highly_divisible_triangular_number import divisibleTriangleNumber

class UnitTests(unittest.TestCase):

    def test4(self):
        actual = type(divisibleTriangleNumber(5))
        expected = type(5)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test1(self):
        actual = divisibleTriangleNumber(5)
        expected = 28
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test2(self):
        actual = divisibleTriangleNumber(23)
        expected = 630
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = divisibleTriangleNumber(167)
        expected = 1385280
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test5(self):
        actual = divisibleTriangleNumber(374)
        expected = 17907120
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test6(self):
        actual = divisibleTriangleNumber(500)
        expected = 76576500
        self.assertEqual(actual, expected, 'Actual v. Expected')

    
if __name__ == "__main__":
    unittest.main()