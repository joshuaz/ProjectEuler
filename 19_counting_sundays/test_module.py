import unittest
from counting_sundays import countingSundays

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(countingSundays(1943, 1946))
        expected = type(6)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = countingSundays(1943, 1946)
        expected = 6
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = countingSundays(1901, 2000)
        expected = 171
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()