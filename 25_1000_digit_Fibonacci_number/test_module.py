from digitFibonacci import digitFibonacci
import unittest

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = digitFibonacci(5)
        expected = 21
        self.assertEqual(type(actual), type(expected), 'Expected an int')

    def test2(self):
        actual = digitFibonacci(5)
        expected = 21
        self.assertEqual(actual, expected, 'Expected an int')

    def test3(self):
        actual = digitFibonacci(10)
        expected = 45
        self.assertEqual(actual, expected, 'Expected an int')

    def test4(self):
        actual = digitFibonacci(15)
        expected = 69
        self.assertEqual(actual, expected, 'Expected an int')

    def test5(self):
        actual = digitFibonacci(20)
        expected = 93
        self.assertEqual(actual, expected, 'Expected an int')
    

if __name__ == "__main__":
    unittest.main()