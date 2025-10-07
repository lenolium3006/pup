import configparser
import os
import math


def calculate(a, b, epsilon=0.0001):
    if not (1e-9 <= epsilon <= 1e-1): 
        raise ValueError("epsilon вне допустимого диапазона")
    if b == 0:
        raise ZeroDivisionError("деление на ноль")
    decimals = max(0, math.ceil(-math.log10(epsilon)))
    return round(a / b, decimals)


def load_params(config_file="settings.ini"):
    if not os.path.exists(config_file):
        raise FileNotFoundError("Файл настроек не найден")
    config = configparser.ConfigParser()
    config.read(config_file)
    if "SETTINGS" not in config or "epsilon" not in config["SETTINGS"]:
        raise ValueError("Некорректный формат файла конфигурации")
    try:
        epsilon = float(config["SETTINGS"]["epsilon"])
    except ValueError:
        raise ValueError("epsilon должно быть числом")
    if not (1e-9 <= epsilon <= 1e-1):
        raise ValueError("epsilon вне допустимого диапазона")
    return epsilon


# Тесты
import pytest

def test_calculate_normal():
    assert calculate(1, 2, epsilon=0.1) == 0.5
    assert calculate(1, 1000, epsilon=0.001) == 0.001


def test_calculate_divide_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(1, 0)


def test_calculate_bad_epsilon():
    with pytest.raises(ValueError):
        calculate(1, 2, epsilon=1)


def test_load_params_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_params("no_such_file.ini")


def test_load_params_bad_format(tmp_path):
    d = tmp_path / "settings.ini"
    d.write_text("[BAD]\nvalue=123")
    with pytest.raises(ValueError):
        load_params(str(d))


def test_load_params_good(tmp_path):
    d = tmp_path / "settings.ini"
    d.write_text("[SETTINGS]\nepsilon=0.001")
    assert load_params(str(d)) == 0.001


def test_load_params_wrong_value(tmp_path):
    d = tmp_path / "settings.ini"
    d.write_text("[SETTINGS]\nepsilon=abc")
    with pytest.raises(ValueError):
        load_params(str(d))


if __name__ == "__main__":

    print("Проверка calculate:")
    print("1 / 2 с epsilon=0.1 =", calculate(1, 2, epsilon=0.1))
    print("1 / 1000 с epsilon=0.001 =", calculate(1, 1000, epsilon=0.001))

    example_ini = "settings.ini"
    with open(example_ini, "w") as f:
        f.write("[SETTINGS]\nepsilon=0.001")

    print("epsilon =:", load_params(example_ini))
