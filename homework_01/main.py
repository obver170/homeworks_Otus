"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    res = [i * i for i in args]
    return res


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    numbers = args[0]
    if ODD in args:
        res = [i for i in numbers if i % 2 != 0]
    elif EVEN in args:
        res = [i for i in numbers if i % 2 == 0]
    else:
        res = [i for i in numbers if is_prime_number(i)]

    return res


def is_prime_number(number):
    # Метод для определения "простоты" числа
    if number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

