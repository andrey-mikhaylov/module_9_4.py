"""
Задача "Функциональное разнообразие"
"""

import random
from typing import Callable, Collection


def test1():
    """
    Lambda-функция
    """
    first = 'Мама мыла раму'
    second = 'Рамена мало было'
    # Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
    # Здесь ? - место написания lambda-функции.
    result = list(map(lambda x, y: x == y, first, second))
    print(result)
    """
    Результатом должен быть список совпадения букв в той же позиции:
    [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
    Где True - совпало, False - не совпало.
    """


def test2():
    """
    Замыкание:
    """

    def get_advanced_writer(file_name: str) -> Callable[[Collection, ...], None]:
        """
        :param file_name: название файла для записи.
        :return: функцию write_everything.
        """

        def write_everything(*data_set: Collection):
            """
            Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
            :param data_set: параметр принимающий неограниченное количество данных любого типа.
            :return:
            """
            with open(file_name, 'a') as f:
                for item in data_set:
                    f.write(str(item) + '\n')

        return write_everything

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    """
    Запишет данные в файл в таком виде:
    Это строчка
    ['А', 'это', 'уже', 'число', 5, 'в', 'списке']
    """


def test3():
    """
    Метод __call__:
    """
    class MysticBall:
        def __init__(self, *words: Collection[str]):
            """
            :param words: коллекция строк
            """
            self.words = words

        def __call__(self) -> str:
            """
            Случайным образом выбирает слово из words
            :return: слово из words
            """
            # Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.
            return random.choice(self.words)

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())

    """
    Примерный результат (может отличаться из-за случайности выбора):
    Да
    Да
    Наверное
    """


if __name__ == '__main__':
    test1()
    test2()
    test3()


"""
2023/12/02 00:00|Домашнее задание по теме "Создание функций на лету"
Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.

Задача "Функциональное разнообразие":
Lambda-функция:
Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.

Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.

Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything.

Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
Запишет данные в файл в таком виде:


Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию choice из модуля random.

Ваш код (количество слов для случайного выбора может быть другое):
from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
Примерный результат (может отличаться из-за случайности выбора):
Да
Да
Наверное

Примечания:
Все задания пишутся в одном модуле.
Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал логику написанного.
Файл module_9_4.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""
