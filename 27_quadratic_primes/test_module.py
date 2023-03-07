from quadraticPrimes import quadraticPrimes
import unittest

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = quadraticPrimes(200)
        expected = -4925
        self.assertEqual(type(actual), type(expected), 'Expected an int')

    def test2(self):
        actual = quadraticPrimes(200)
        expected = -4925
        self.assertEqual(actual, expected, 'Expected an int')

    def test3(self):
        actual = quadraticPrimes(500)
        expected = -18901
        self.assertEqual(actual, expected, 'Expected an int')

    def test4(self):
        actual = quadraticPrimes(800)
        expected = -43835
        self.assertEqual(actual, expected, 'Expected an int')

    def test5(self):
        actual = quadraticPrimes(1000)
        expected = -59231
        self.assertEqual(actual, expected, 'Expected an int')
    

if __name__ == "__main__":
    unittest.main()