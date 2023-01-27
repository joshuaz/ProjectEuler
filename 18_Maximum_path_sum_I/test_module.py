import unittest
from maximum_path_sum_I import maximumPathSumI
from maximum_path_sum_I import testTriangle, numTriangle

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(maximumPathSumI(testTriangle))
        expected = type(23)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = maximumPathSumI(testTriangle)
        expected = 23
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = maximumPathSumI(numTriangle)
        expected = 1074
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()