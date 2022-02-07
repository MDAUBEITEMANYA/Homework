import filecmp
import hashlib
import os
from collections import Counter
import pandas as pandasForSortingCSV


def file_find_name():
    my_file = open("unsorted_names.txt", "r")
    names_list = my_file.readlines()
    names_list = sorted(set(names_list))
    print(names_list)
    my_file.close()
    return names_list


def file_write(names_list: list):
    with open("unsorted_names.txt", "r") as my_file:
        my_file.writelines(names_list)


# file_write(file_find_name())

def most_common_words(filepath, number_of_words):
    with open(filepath, "r") as my_file:
        word_list = []
        for line in my_file:
            tpm_line = line.lower().split()
            word_list.extend(tpm_line)
        word_list = word_list
        count = Counter(word_list)
    return count.most_common(number_of_words)


# print(most_common_words('lorem_ipsum.txt', 3))


def get_top_performers(file_path, number_of_top_students):
    my_file = open(file_path, "r")
    word_dict = {}
    for line in my_file:
        tpm_line = line.lower().strip("\n").split(',')
        word_dict[tpm_line[0]] = tpm_line[2]
    sorted_dict = {}
    sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)
    return sorted_dict


print(get_top_performers('students.csv', 3))


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def get_top_performers_write_scv(file_path, number_of_top_students):
    # USE THIS LINE TO ADD TO LINE TO SCV FILE line_prepender('students.csv', 'student name,age,average mark')
    csvData = pandasForSortingCSV.read_csv(file_path)
    print(csvData)
    csvData.sort_values(["age"],
                        axis=0,
                        ascending=[False],
                        inplace=True)
    csvData.to_csv("sorted_students_age.csv")

    # my_file = open("sorted_students.scv", "a")
    # my_file.write(csvData)
    # my_file.close()

    # print(get_top_performers('students.csv', 3))

    # filecmp.cmp(f1, f2, shallow=True)

    # print_duplicates('dz')


prev_output = None


def show_previous_result(func):
    def inner(string):
        global prev_output
        if not prev_output:
            print("Previous Result:", None)
        if prev_output:
            print("previous res:", prev_output)

        prev_output = str(func(string)) + "\n"

        print("new res", func(string))

        return func(string)

    return inner


### Task 4.5
@show_previous_result
def print_duplicates(dir):
    unique = []
    duplicates = []
    dir_files = os.listdir(dir)
    files_length = len(os.listdir(dir))
    for i in range(files_length):
        for j in range(i + 1, files_length):
            if filecmp.cmp(dir + '/' + str(dir_files[i]), dir + '/' + str(dir_files[j]), shallow=True):
                duplicates.append((str(dir_files[i]) + " and " + str(dir_files[j]) + " are duplicated by content"))
    return duplicates


#print_duplicates('dz')
#print_duplicates('dz')


### Task 4.5
def memoize(function):
    memo = None

    def wrapper(*args, **kwargs):
        nonlocal memo
        if memo:
            return memo
        else:
            result = function(*args)
            memo = result
            return result

    return wrapper


@memoize
def summarise(a, b):
    return a + b


# print(summarise(1, 2))
# print(summarise(1, 3))
# print(summarise(1, 2))
# print(summarise(1, 100))


def validate(low_bound, upper_bound):
    def my_decorator(func):
        def wrapper(args):
            for x in args:
                if x < low_bound or x > upper_bound:
                    return 'Function call is no valid!'
            return func(args)

        return wrapper

    return my_decorator


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    return "Pixel created!"

# print(set_pixel((0, 127, 300)))
# print(set_pixel((0, 127, 250)))
