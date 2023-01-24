import unittest
from power_digit_sum import powerDigitSum

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(powerDigitSum(15))
        expected = type(26)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = powerDigitSum(15)
        expected = 26
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = powerDigitSum(128)
        expected = 166
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test4(self):
        actual = powerDigitSum(1000)
        expected = 1366
        self.assertEqual(actual, expected, 'Actual v. Expected')  

if __name__ == "__main__":
    unittest.main()