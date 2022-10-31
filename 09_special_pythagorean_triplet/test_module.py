import unittest
from special_pythagorean_triplet import special_pythagorean_triplet


class UnitTests(unittest.TestCase):

    def test4(self):
        actual = type(special_pythagorean_triplet(24))
        expected = type(24)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test1(self):
        actual = special_pythagorean_triplet(24)
        expected = 480
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test2(self):
        actual = special_pythagorean_triplet(120)
        expected = 60000
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = special_pythagorean_triplet(1000)
        expected = 31875000
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
if __name__ == "__main__":
    unittest.main()