class TestCalculate(unittest.TestCase):

    def test_half(self):
        self.assertEqual(calculate(1, 2, 0.01), 0.5)

    def test_thousand(self):
        self.assertEqual(calculate(1, 1000, 0.001), 0.001)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(1, 0)

    def test_epsilon_range(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, 1)

    def test_wrong_format(self):
        with self.assertRaises(ValueError):
            float("abc")