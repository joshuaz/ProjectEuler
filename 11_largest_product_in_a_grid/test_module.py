import unittest
from largest_product_in_a_grid import largestGridProduct, grid, testGrid
import pandas as pd

class UnitTests(unittest.TestCase):

    def test4(self):
        actual = type(largestGridProduct(testGrid))
        expected = type(14169081)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test1(self):
        actual = largestGridProduct(testGrid)
        expected = 14169081
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test2(self):
        actual = largestGridProduct(grid)
        expected = 70600674
        self.assertEqual(actual, expected, 'Actual v. Expected')

    
if __name__ == "__main__":
    unittest.main()