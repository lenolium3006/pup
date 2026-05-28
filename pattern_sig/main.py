import requests
import time
from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt


class SingletonMeta(type):
    """
    Метакласс Singleton.
    """

    _instance = None

    def __call__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class CurrenciesLst(metaclass=SingletonMeta):
    """
    Класс для работы с валютами.
    """

    def __init__(self, delay=1):

        self.__cur_lst = []
        self.__delay = delay
        self.__last_request_time = 0

    def __del__(self):
        """
        Деструктор класса.
        """

        self.__cur_lst.clear()

    def get_currencies(self, currencies_ids_lst: list) -> list:
        """
        Получение курсов валют.
        """

        current_time = time.time()

        if current_time - self.__last_request_time < self.__delay:
            raise Exception("Слишком частые запросы")

        self.__last_request_time = current_time

        response = requests.get(
            'http://www.cbr.ru/scripts/XML_daily.asp'
        )

        root = ET.fromstring(response.content)

        result = []

        for valute in root.findall("Valute"):

            valute_id = valute.get('ID')

            if valute_id in currencies_ids_lst:

                name = valute.find('Name').text
                value = valute.find('Value').text
                char_code = valute.find('CharCode').text
                nominal = valute.find('Nominal').text

                integer_part, fractional_part = value.split(',')

                result.append({
                    char_code: (
                        name,
                        (integer_part, fractional_part),
                        nominal
                    )
                })

        for currency_id in currencies_ids_lst:

            found = False

            for item in result:
                if currency_id in str(item):
                    found = True

            if not found:
                result.append({currency_id: None})

        self.__cur_lst = result

        return result

    def get_cur_lst(self):
        """
        Геттер списка валют.
        """

        return self.__cur_lst

    def set_delay(self, delay):
        """
        Сеттер задержки запросов.
        """

        self.__delay = delay

    def visualize_currencies(self):
        """
        Построение графика валют.
        """

        currencies = []
        values = []

        for item in self.__cur_lst:

            for key, value in item.items():

                if value is not None:

                    currencies.append(key)

                    integer_part = value[1][0]
                    fractional_part = value[1][1]

                    full_value = float(
                        integer_part + "." + fractional_part
                    )

                    values.append(full_value)

        plt.bar(currencies, values)

        plt.title("Курсы валют")

        plt.savefig("currencies.jpg")

        plt.show()


if __name__ == '__main__':

    currencies = CurrenciesLst()

    result = currencies.get_currencies(
        ['R01035', 'R01335', 'R01700J']
    )

    print(result)

    currencies.visualize_currencies()