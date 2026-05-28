
from abc import ABC, abstractmethod
from typing import Dict, Any
import requests
import yaml
import csv


class Component(ABC):
    """
    Базовый интерфейс компонента.
    """

    @abstractmethod
    def operation(self) -> Any:
        """
        Метод получения данных.
        """
        pass

    @abstractmethod
    def save_to_file(self, filename: str) -> None:
        """
        Метод сохранения данных в файл.
        """
        pass


class ConcreteComponent(Component):
    """
    Базовый компонент, возвращающий JSON.
    """

    def __init__(self):

        self.url = "https://www.cbr-xml-daily.ru/daily_json.js"

    def operation(self) -> Dict:
        """
        Получение JSON с API ЦБ РФ.
        """

        response = requests.get(self.url)

        return response.json()

    def save_to_file(self, filename: str) -> None:
        """
        Сохранение JSON в файл.
        """

        data = self.operation()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(data))


class Decorator(Component):
    """
    Базовый класс декоратора.
    """

    def __init__(self, component: Component):

        self._component = component

    def operation(self) -> Any:

        return self._component.operation()

    def save_to_file(self, filename: str) -> None:

        self._component.save_to_file(filename)


class YamlDecorator(Decorator):
    """
    Декоратор YAML.
    """

    def operation(self) -> str:
        """
        Преобразование данных в YAML.
        """

        data = self._component.operation()

        return yaml.dump(
            data,
            allow_unicode=True
        )

    def save_to_file(self, filename: str) -> None:
        """
        Сохранение YAML в файл.
        """

        data = self.operation()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)


class CsvDecorator(Decorator):
    """
    Декоратор CSV.
    """

    def operation(self) -> list:
        """
        Преобразование данных в CSV формат.
        """

        data = self._component.operation()

        currencies = []

        for key, value in data["Valute"].items():

            currencies.append([
                key,
                value["Name"],
                value["Value"]
            ])

        return currencies

    def save_to_file(self, filename: str) -> None:
        """
        Сохранение CSV в файл.
        """

        data = self.operation()

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Code",
                "Name",
                "Value"
            ])

            writer.writerows(data)


def client_code(component: Component) -> None:
    """
    Клиентский код.
    """

    result = component.operation()

    print(result)


if __name__ == "__main__":

    simple = ConcreteComponent()

    print("JSON:")
    client_code(simple)

    yaml_component = YamlDecorator(simple)

    print("\nYAML:")
    client_code(yaml_component)

    csv_component = CsvDecorator(simple)

    print("\nCSV:")
    client_code(csv_component)

    yaml_component.save_to_file("currencies.yaml")

    csv_component.save_to_file("currencies.csv")