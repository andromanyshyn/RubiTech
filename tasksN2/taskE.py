# Написать класс, принимающий на вход текст.
# Один метод класса должен выводить в консоль самое длинное слово в тексте.
# Второй метод - самое часто встречающееся слово.
# Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее).
# Четвертый метод выводит все палиндромы через запятую.


import time
from string import punctuation


def timer(method):
    def wrapper(self):
        start = time.time()
        result = method(self)
        end = time.time()
        print(f'Time of method is {end - start}')
        print()
        return result

    return wrapper


class Text:
    def __init__(self, text):
        self.text = text

    @timer
    def longest_word(self):
        time.sleep(2)
        return f"Longest word in text: {max(self.text.split(), key=len)}"

    @timer
    def repeat_word(self):
        text = self.text.split()
        max_number = 0
        dict_of_words = {}
        often_word = None
        for word in text:
            if word not in dict_of_words:
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1

            if dict_of_words[word] > max_number:
                often_word = word
                max_number = dict_of_words[word]

        return f"Most repeated word in text: {often_word}"

    @timer
    def punctuation_symbols(self):
        symbols_list = [symbol for symbol in self.text if symbol in punctuation]
        return f"Symbols in text: {len(symbols_list)}"

    @timer
    def palindroms(self):
        palindorm_list = list(filter(lambda x: x == x[::-1], self.text.split()))
        return f"Palindroms in text: {','.join(palindorm_list)}"


text = Text('python python java java java c++ #$%@! anna wwww')
print(text.longest_word())
print(text.repeat_word())
print(text.punctuation_symbols())
print(text.palindroms())
