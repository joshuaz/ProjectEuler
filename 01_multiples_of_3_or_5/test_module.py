import unittest
from multiples_of_3_or_5 import sum_of_multiples


class UnitTests(unittest.TestCase):

    def should_return_number(self):
        actual = type(sum_of_multiples(10))
        expected = type(34)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def Forty_nine_should_return_543(self):
        actual = sum_of_multiples(49)
        expected = 543
        self.assertEqual(actual, expected, 'Expected calling "sum_of_multiples()" with 49 should return 543')

    def thousand_should_return_233168(self):
        actual = sum_of_multiples(1000)
        expected = 233168
        self.assertEqual(actual, expected, 'Expected calling "sum_of_multiples()" with 1000 should return 233168')

    def test4(self):
        actual = sum_of_multiples(8456)
        expected = 16687353
        self.assertEqual(actual, expected, 'Expected calling "sum_of_multiples()" with 8456 should return 16687353')

    def test5(self):
        actual = sum_of_multiples(19564)
        expected = 89301183
        self.assertEqual(actual, expected, 'Expected calling "sum_of_multiples()" with 19564 should return 89301183')

if __name__ == "__main__":
    unittest.main()