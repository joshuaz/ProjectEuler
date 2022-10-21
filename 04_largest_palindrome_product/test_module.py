import unittest
from largest_palindrome_product import largest_palindrome_product, isPalindrome


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(largest_palindrome_product(2))
        expected = type(9009)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    

    def test1(self):
        actual = largest_palindrome_product(2)
        expected = 9009
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = largest_palindrome_product(3)
        expected = 906609
        self.assertEqual(actual, expected, 'Actual v. Expected')

if __name__ == "__main__":
    unittest.main()