import unittest

def calculate(a, b, epsilon=0.0001):
    if b == 0:
        print("Ошибка: деление на ноль")
        return None
    return round(a / b, 4)


def load_params(filename="settings.ini"):
    try:
        f = open(filename, "r")
        for line in f:
            if "epsilon" in line:
                parts = line.split("=")
                f.close()
                return float(parts[1])
        f.close()


class TestAll(unittest.TestCase):
    def test_division_half(self):
        self.assertEqual(calculate(1, 2, 0.1), 0.5)

    def test_small_division(self):
        self.assertEqual(calculate(1, 1000, 0.001), 0.001)

    def test_divide_by_zero(self):
        self.assertIsNone(calculate(1, 0))

    def test_load_value(self):
        # создадим временный файл для теста
        with open("settings.ini", "w") as f:
            f.write("epsilon = 0.001\n")
        e = load_params("settings.ini")
        self.assertEqual(e, 0.001)

    def test_file_not_found(self):
        e = load_params("nofile.ini")
        self.assertIsNone(e)


if __name__ == "__main__":
    unittest.main()

