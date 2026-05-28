import unittest
from main import CurrenciesLst

class TestCurrencies(unittest.TestCase):

    def setUp(self):
        self.currencies = CurrenciesLst()
        self.currencies.set_delay(0)   # отключаем защиту от частых запросов

    def test_wrong_id(self):
        result = self.currencies.get_currencies(['R9999'])
        self.assertEqual(result, [{'R9999': None}])

    def test_gbp_currency(self):
        result = self.currencies.get_currencies(['R01035'])
        currency = result[0]['GBP'][0]
        self.assertEqual(currency, 'Фунт стерлингов Соединенного королевства')

    def test_currency_value_range(self):
        result = self.currencies.get_currencies(['R01035'])
        integer_part = int(result[0]['GBP'][1][0])
        self.assertTrue(0 <= integer_part <= 999)

if __name__ == '__main__':
    unittest.main()