# Написать класс, принимающий на вход текст.
# Один метод класса должен выводить в консоль самое длинное слово в тексте.
# Второй метод - самое часто встречающееся слово.
# Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее).
# Четвертый метод выводит все палиндромы через запятую.


import time
from string import punctuation


def timer(method):
    def wrapper(text):
        start = time.time()
        result = method(text)
        end = time.time()
        print(f'Time of method is {end - start}')
        print()
        return result

    return wrapper


class Text:

    @staticmethod
    @timer
    def longest_word(text):
        # time.sleep(2)
        return max(text.split(), key=len)

    @staticmethod
    @timer
    def repeat_word(text):
        text = text.split()
        max = 0
        for word in text:
            if text.count(word) > max:
                often_word = word
                max = text.count(word)
        return often_word

    @staticmethod
    @timer
    def punctuation_symbols(text):
        symbols_list = [symbol for symbol in text if symbol in punctuation]
        return len(symbols_list)

    @staticmethod
    @timer
    def palindroms(text):
        palindorm_list = list(filter(lambda x: x == x[::-1], text.split()))
        return ','.join(palindorm_list)


# print(Text.longest_word('Один метод класса должен выводить в консоль самое длинное слово в тексте'))
# print(Text.repeat_word('python python java java java c++'))
# print(Text.punctuation_symbols('Третий,, метод./ выводит $%^ количество,,. спецсимволов в тексте'))
# print(Text.palindroms('bob ded oko word message hello pink'))
