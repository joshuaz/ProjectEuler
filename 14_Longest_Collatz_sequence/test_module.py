import unittest
from longest_collatz_sequence import longestCollatzSequence


class UnitTests(unittest.TestCase):

    def test1(self):
        actual = type(longestCollatzSequence(14))
        expected = type(14)
        self.assertEqual(type(actual), type(expected), 'Expected an int')
    
    def test2(self):
        actual = longestCollatzSequence(14)
        expected = 9
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test3(self):
        actual = longestCollatzSequence(5847)
        expected = 3711
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test4(self):
        actual = longestCollatzSequence(46500)
        expected = 35655
        self.assertEqual(actual, expected, 'Actual v. Expected')

    def test5(self):
        actual = longestCollatzSequence(54512)
        expected = 52527
        self.assertEqual(actual, expected, 'Actual v. Expected')
     
    def test6(self):
        actual = longestCollatzSequence(100000)
        expected = 77031
        self.assertEqual(actual, expected, 'Actual v. Expected')
    
    def test7(self):
        actual = longestCollatzSequence(1000000)
        expected = 837799
        self.assertEqual(actual, expected, 'Actual v. Expected')
     
if __name__ == "__main__":
    unittest.main()