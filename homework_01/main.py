# """
# Домашнее задание №1
# Функции и структуры данных
# """


def is_prime(num):
    if num == 1 or num ==0:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def power_numbers(*args):
    list = [*args]
    list = [el ** 2 for el in list[:]]
    return list

    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list, filter_type):
    final = []
    if filter_type == ODD:
        for i in list:
            if i % 2 != 0:
                final.append(i)
    elif filter_type == EVEN:
        for i in list:
            if i % 2 == 0:
                final.append(i)
    elif filter_type == PRIME:
        for i in list:
            if is_prime(i):
                final.append(i)
    return final

    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """
