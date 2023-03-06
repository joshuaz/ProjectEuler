import itertools
from lexical_permutations import lexical_permutations
import unittest

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = lexical_permutations(699999)
        expected = 1938246570
        self.assertEqual(type(actual), type(expected), 'Expected an int')

    def test2(self):
        actual = lexical_permutations(699999)
        expected = 1938246570
        self.assertEqual(actual, expected, 'Expected an int')

    def test3(self):
        actual = lexical_permutations(899999)
        expected = 2536987410
        self.assertEqual(actual, expected, 'Expected an int')

    def test4(self):
        actual = lexical_permutations(900000)
        expected = 2537014689
        self.assertEqual(actual, expected, 'Expected an int')

    def test5(self):
        actual = lexical_permutations(999999)
        expected = 2783915460
        self.assertEqual(actual, expected, 'Expected an int')
    

if __name__ == "__main__":
    unittest.main()