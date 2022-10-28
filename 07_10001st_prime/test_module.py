import unittest
from what_is_the_10001st_prime import what_is_the_10001st_prime


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(what_is_the_10001st_prime(6))
        expected = type(6)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = what_is_the_10001st_prime(6)
        expected = 13
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = what_is_the_10001st_prime(10)
        expected = 29
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = what_is_the_10001st_prime(100)
        expected = 541
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test5(self):
        actual = what_is_the_10001st_prime(1000)
        expected = 7919
        self.assertEqual(actual, expected, 'Actual v. Expected')
   
    def test6(self):
        actual = what_is_the_10001st_prime(10001)
        expected = 104743
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()