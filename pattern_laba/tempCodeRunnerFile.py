import unittest

from main import (
    ConcreteComponent,
    YamlDecorator,
    CsvDecorator
)


class TestCurrencies(unittest.TestCase):

    def test_json_response(self):

        component = ConcreteComponent()

        result = component.operation()

        self.assertIn("Valute", result)

    def test_json_type(self):

        component = ConcreteComponent()

        result = component.operation()

        self.assertIsInstance(result, dict)

    def test_yaml_response(self):

        component = YamlDecorator(
            ConcreteComponent()
        )

        result = component.operation()

        self.assertIsInstance(result, str)

    def test_yaml_contains_currency(self):

        component = YamlDecorator(
            ConcreteComponent()
        )

        result = component.operation()

        self.assertIn("USD", result)

    def test_csv_response(self):

        component = CsvDecorator(
            ConcreteComponent()
        )

        result = component.operation()

        self.assertIsInstance(result, list)

    def test_csv_contains_data(self):

        component = CsvDecorator(
            ConcreteComponent()
        )

        result = component.operation()

        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()