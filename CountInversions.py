__author__ = 'kati'
"""
     В комьютерной науке и дискретной математике, инверсия - это пара позиций последовательности, где элементы на этих позициях выпадают из естественного порядка. Таким образом, если мы используем порядок по возрастанию для группы чисел, то инверсия получается, когда более крупные цифры стоят перед меньшим значением в последовательности.

Проверим такой пример последовательности: (1, 2, 5, 3, 4, 7, 6) и мы можем видеть здесь три инверсии
- 5 и 3; - 5 и 4; - 7 и 6.

Вам дана последовательность уникальных чисел и вы должны подсчитать число инверсий в этой последовательности.

Входные данные: Последовательность как кортеж целых чисел.

Выходные данные: Количество инверсий.

Предусловия: 2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)
"""
def count_inversion(sequence):
    sum = 0
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] > sequence[j]:
                sum += 1
            else:
                sum += 0
    return sum

    """
        Count inversions in a sequence of numbers
    """
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"