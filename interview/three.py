from collections.abc import Iterable
import re

# 3.0
from math import prod
from typing import List


def intersect(*args: Iterable):
    if len(args) > 0:
        final = set(args[0])
        for x in args:
            final = final.intersection(set(x))
        return final
    return {}


# 3.0
def union(*args: Iterable):
    if len(args) > 0:
        final = set(args[0])
        for x in args:
            final = final.union(set(x))
        return final
    return {}


# print(intersect())
# print(union([1, 2, 3], (1, 4)))


# 3.1
def convert_string(string):
    if len(string) > 0:
        output = ord(string[-1])
        for x in reversed(string[:-1]):
            number = ord(x)
            output = output + (number * (10 ** (len(str(output)))))
    return output


# print(convert_string('abcd'))

# 3.3
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


# print(is_palindrome('stanley Yelnats'))
# print(is_palindrome('starnley Yelnats'))

# 3.4
def split_strings(sentence: str, separator=" "):
    split_value = []
    tmp = ''
    for x in sentence:
        if x == separator:
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += x
    if tmp:
        split_value.append(tmp)
    return split_value


# print(split_strings('123', '2'))

# 3.5
def split_by_index(sentence: str, indexes: List[int]):
    split_value = []
    indexes = sorted(indexes)

    if len(indexes) < 1 or indexes[0] >= len(sentence):
        split_value.append(sentence)
        return split_value

    start_position = 0
    for x in indexes:
        if x >= len(sentence):
            return split_value
        if x == start_position:
            continue
        print(sentence[start_position:x])
        split_value.append(sentence[start_position:x])
        start_position = x
    split_value.append(sentence[start_position:])

    return split_value


# print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# 3.6
def get_digits(num: int):
    tmp_int = num
    my_list = []
    while tmp_int > 0:
        my_list.append(tmp_int % 10)
        tmp_int = tmp_int // 10
    my_list.reverse()
    return tuple(my_list)


# print(get_digits(87178291199))


# 3.7
def get_longest_word(sentence: str):
    longest = max(sentence.split(), key=len)
    return longest

    # print(get_longest_word('Python is simple and effective!'))

    # 3.8


def foo(input_list: list):
    mul = prod(input_list)
    return [int(mul / x) for x in input_list]


print(foo([3, 2, 1]))


# 3.9
def get_pairs(lst: List):
    final_list = []
    for x in range(len(lst) - 1):
        first = [lst[x]]
        second = [lst[x + 1]]
        zip_list = zip(first, second)
        final_list.append(list(zip_list)[0])
    return final_list


# print(get_pairs(['need', 'to', 'sleep', 'more']))

# 3.10
def find_characters(*my_strings: List[str]):
    return set.intersection(*map(set, my_strings)) if my_strings else set()


def find_characters_least_one(my_strings: List[str]):
    character_list = []
    for i in my_strings:
        for j in i:
            character_list.append(j)
    character_list = list(set(character_list))
    character_list.sort()
    return character_list


def find_two_characters(my_strings: List[str]):
    character_dict = {}
    character_list = []
    if len(my_strings) < 2:
        return None
    my_doll = map(set, my_strings)
    for i in my_doll:
        for key in i:
            if key in character_dict:
                character_dict[key] = character_dict[key] + 1
            else:
                character_dict[key] = 1
    for key in character_dict:
        if character_dict[key] > 1:
            character_list.append(key)
    character_list.sort()
    return character_list


import string


def find_characters_alphabet(my_strings: List[str]):
    in_strings = find_characters_least_one(my_strings)
    alphabet = list(string.ascii_lowercase)
    for i in in_strings:
        alphabet.remove(i)
    return alphabet


test_strings = ["hello", "world", "python", ]
print(find_two_characters(test_strings))
print(find_characters_alphabet(test_strings))


# print(find_characters(*test_strings))


# 3.11
def generate_squares(number):
    return {i: i ** 2 for i in range(1, number + 1)}


# print(generate_squares(5))


# print(join_two_dict({"a": {"b": "c"}}, {"a": {"e": "d"}, "b": {"1": "2"}}))

# Task 3.12
def combine_dicts(*args: dict):
    final_dict = {}
    for x in args:
        for key in x:
            if key in final_dict:
                final_dict[key] = final_dict[key] + x[key]
            else:
                final_dict[key] = x[key]
    return final_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2))
# print(combine_dicts(dict_1, dict_2, dict_3))
