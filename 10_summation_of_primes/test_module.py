import unittest
from summation_of_primes import primeSummation


class UnitTests(unittest.TestCase):

    def test4(self):
        actual = type(primeSummation(17))
        expected = type(41)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test1(self):
        actual = primeSummation(2001)
        expected = 277050
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test2(self):
        actual = primeSummation(140759)
        expected = 873608362
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = primeSummation(2000000)
        expected = 142913828922
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
if __name__ == "__main__":
    unittest.main()