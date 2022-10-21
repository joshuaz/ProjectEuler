import unittest
from even_fibonacci_numbers import fib


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(fib(10))
        expected = type(10)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = fib(10)
        expected = 10
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = fib(60)
        expected = 44
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = fib(1000)
        expected = 798
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test5(self):
        actual = fib(100000)
        expected = 60696
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test6(self):
        actual = fib(4000000)
        expected = 4613732
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()