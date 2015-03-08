# coding=utf-8
__author__ = 'kati'
"""
    Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
    Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

    Входные данные: Положительное целое число.
    Выходные данные: Произведение цифр как целочисленное (int).
    Предусловия: 0 < number < 106
"""

def checkio(number):
    num = str(number)
    n = 1
    for i in num:
        if int(i) != 0:
            n *= int(i)
    return n

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
