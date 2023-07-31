# B. Реализовать функцию, принимающую два списка и возвращающую словарь
# (ключ из первого списка, значение из второго), упорядоченный по ключам.
# Результат вывести в консоль.
# Длина первого списка не должна быть равна длине второго.
# Результат вывести в консоль.


def get_dict(lst1, lst2):
    if len(lst1) == len(lst2):
        raise ValueError('The length of the first list should not be equal to the length of the second')
    d_dict = {key: value for key, value in zip(sorted(lst1), lst2)}
    return d_dict


print(get_dict([5, 2], ['andrew', 'petya', 'vasya']))


