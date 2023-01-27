import unittest
from number_letter_counts import numberLetterCounts
import inflect

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(numberLetterCounts(5))
        expected = type(19)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = numberLetterCounts(5)
        expected = 19
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = numberLetterCounts(150)
        expected = 1903
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = numberLetterCounts(1000)
        expected = 21124
        self.assertEqual(actual, expected, 'Actual v. Expected')  

if __name__ == "__main__":
    unittest.main()