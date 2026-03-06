from fibonacci import FibonacchiLst
import unittest

class TestFibIterator(unittest.TestCase):

    def test_normal(self):
        result = FibonacchiLst(list(range(10)))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])

    def test_corner_0(self):
        result = FibonacchiLst(list(range(0)))
        self.assertEqual(result, [])

    def test_corner_1(self):
        result = FibonacchiLst(list(range(1)))
        self.assertEqual(result, [0])

    def test_corner_2(self):
        result = FibonacchiLst(list(range(2)))
        self.assertEqual(result, [0, 1])

    def test_corner_3(self):
        result = FibonacchiLst(list([1, 1]))
        self.assertEqual(result, [1, 1])

