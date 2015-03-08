#coding=utf-8
"""
     Давайте научим наших роботов отличать слова от чисел.
    Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят
    только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one
    two three 7 end" есть три слова подряд.

    Входные данные: Строка со словами (str).
    Выходные данные: Ответ как логическое выражение (bool), True или False.
    Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
    0 < len(words) < 100
"""

def checkio(words):
    count=0
    word = words.split(' ')
    for i in word:
        if i.isalpha():
            count += 1
        else:
            count = 0
        if count >= 3:
            return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
