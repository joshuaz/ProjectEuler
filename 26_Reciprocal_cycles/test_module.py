from reciprocalCycles import reciprocalCycles
import unittest

class UnitTests(unittest.TestCase):

    def test1(self):
        actual = reciprocalCycles(700)
        expected = 659
        self.assertEqual(type(actual), type(expected), 'Expected an int')

    def test2(self):
        actual = reciprocalCycles(700)
        expected = 659
        self.assertEqual(actual, expected, 'Expected an int')

    def test3(self):
        actual = reciprocalCycles(800)
        expected = 743
        self.assertEqual(actual, expected, 'Expected an int')

    def test4(self):
        actual = reciprocalCycles(900)
        expected = 887
        self.assertEqual(actual, expected, 'Expected an int')

    def test5(self):
        actual = reciprocalCycles(1000)
        expected = 983
        self.assertEqual(actual, expected, 'Expected an int')
    

if __name__ == "__main__":
    unittest.main()