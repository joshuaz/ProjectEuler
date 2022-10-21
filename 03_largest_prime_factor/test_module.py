import unittest
from largest_prime_factor import largest_prime_factor


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(largest_prime_factor(2))
        expected = type(2)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = largest_prime_factor(2)
        expected = 2
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = largest_prime_factor(3)
        expected = 3
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = largest_prime_factor(5)
        expected = 5
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test5(self):
        actual = largest_prime_factor(7)
        expected = 7
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test6(self):
        actual = largest_prime_factor(8)
        expected = 2
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test7(self):
        actual = largest_prime_factor(13195)
        expected = 29
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()