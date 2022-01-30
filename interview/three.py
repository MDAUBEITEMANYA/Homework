from collections.abc import Iterable
import re

# 3.0
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
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


# print(is_palindrome('stanley Yelnats'))

# 3.4
def split_strings(sentence: str):
    split_value = []
    tmp = ''
    for x in sentence:
        if x == ' ':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += x
    if tmp:
        split_value.append(tmp)
    return split_value


# print(split_strings('This is a sentence'))

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

# 3.7
def get_longest_word(sentence: str):
    longest = max(sentence.split(), key=len)
    return longest


# print(get_longest_word('Python is simple and effective!'))

# 3.8
def foo(my_list: List[int]):
    output_list = []
    for x in range(len(my_list)):
        final_num = 1
        for i in range(len(my_list)):
            if i == x:
                continue
            final_num = final_num * my_list[i]
        output_list.append(final_num)
    return output_list


# print( foo([3, 2, 1]))

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


test_strings = ["hello", "world", "python", ]


# print(find_characters(*test_strings))


# 3.11
def generate_squares(number):
    return {i: i ** 2 for i in range(1, number + 1)}


# print(generate_squares(5))

# 3.14

def join_two_dict(*args: dict):
    final_dict = {}
   # for x in args:


#  for x in dict1():

#  d4.update(dict2)
# return d4


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

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
