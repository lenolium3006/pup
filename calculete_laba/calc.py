import os
import configparser


def calculate(a, b, epsilon=0.0001):
    if not (10**-9 < epsilon < 10**-1):
        raise ValueError("epsilon вне допустимого диапазона")

    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")

    result = a / b

    return round(result, len(str(epsilon).split(".")[1]))


import configparser
import os


def load_params():

    config = configparser.ConfigParser()

    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, "settings.ini")

    if not config.read(config_path):
        raise FileNotFoundError("Файл settings.ini не найден")

    epsilon = float(config["SETTINGS"]["epsilon"])

    return epsilon


if __name__ == "__main__":

    epsilon = load_params()

    result = calculate(1, 2, epsilon)

    print(result)