import unittest

from taskB import get_dict
from taskE import Text


# TaskB
class TestB(unittest.TestCase):

    def test_result_success(self):
        self.assertEqual(get_dict([5, 2], ['andrew', 'petya', 'vasya']),
                         {2: 'andrew', 5: 'petya'})

        self.assertEqual(get_dict([1], ['London', 'Warsaw']),
                         {1: 'London'})

        self.assertEqual(get_dict(['Yellow', 'Red'], ['Blue', 'White', 'Green']),
                         {'Red': 'Blue', 'Yellow': 'White'})

    def test_result_failed(self):
        self.assertEqual(get_dict([5, 2, 3], ['andrew', 'petya', 'vasya']),
                         'The length of the first list should not be equal to the length of the second')


# TaskE
class TestTaskE(unittest.TestCase):
    def setUp(self):
        self.text = Text()

    def test_result_success(self):
        self.assertEqual(self.text.longest_word('longestword word ol liam oil getter'), 'longestword')
        self.assertEqual(self.text.repeat_word('python python java java java c++'), 'java')
        self.assertEqual(self.text.punctuation_symbols('example,, punktu., *%$ valute,/'), 9)
        self.assertEqual(self.text.palindroms('bob ded oko word message hello pink'), 'bob,ded,oko')

    def test_result_failed(self):
        self.assertNotEqual(self.text.longest_word('longestword word ol liam oil getter'), 'oil')
        self.assertNotEqual(self.text.repeat_word('python python java java java c++'), 'python')
        self.assertNotEqual(self.text.punctuation_symbols('example,, punktu., *%$ valute,/'), 15)
        self.assertNotEqual(self.text.palindroms('bob ded oko word message hello pink'), 'bob,ded,oko,pink')
