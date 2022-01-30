import filecmp
import hashlib
import os
from collections import Counter
import pandas as pandasForSortingCSV


def file_find_name():
    my_file = open("unsorted_names.txt", "r")
    names_list = []
    for line in my_file:
        names_list.append(line)
    names_list = sorted(set(names_list))
    print(names_list)
    my_file.close()
    return names_list


def file_write(names_list: list):
    my_file = open("sorted_names.txt", "a")
    for name in names_list:
        my_file.write(name)
    my_file.close()


# file_write(file_find_name())

def most_common_words(filepath, number_of_words):
    my_file = open(filepath, "r")
    word_list = []
    for line in my_file:

        tpm_line = line.lower().split()
        for word in tpm_line:
            word_list.append(word)
    word_list = tuple(word_list)
    count = Counter(word_list)
    return count.most_common(number_of_words)


# print(most_common_words('lorem_ipsum.txt', 3))


def get_top_performers(file_path, number_of_top_students):
    my_file = open(file_path, "r")
    word_dict = {}
    for line in my_file:
        tpm_line = line.lower().replace('\n', '').split(',')
        word_dict[tpm_line[0]] = tpm_line[2]
    sorted_dict = {}
    sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)
    counter = 0
    for w in sorted_keys:
        sorted_dict[w] = word_dict[w]
        counter = counter + 1
        if counter == number_of_top_students:
            return sorted_dict


# print(get_top_performers('students.csv', 3))
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def get_top_performers_scv(file_path, number_of_top_students):
    # line_prepender('students.csv', 'student name,age,average mark')
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
def prev_res(func):
    with open('output.txt', "a") as f:
        try:
            prev_output = f.readlines()
        except:
            prev_output = []

    def inner(string):

        if not prev_output: print("Previous Result:", None)
        if prev_output:
            for item in prev_output: print("previous res:", item)

        with open('output.txt', 'a') as file:
            file.write(str(func(string)) + "\n")

        print("new res", func(string))

        return func(string)

    return inner


### Task 4.5
@prev_res
def print_duplicates(dir):
    unique = []
    duplicates = []
    dir_files = os.listdir(dir)
    files_length = len(os.listdir(dir))
    for x in range(files_length):
        for i in range(x + 1, files_length):
            if filecmp.cmp(dir + '/' + str(dir_files[x]), dir + '/' + str(dir_files[i]), shallow=True):
                duplicates.append((str(dir_files[x]) + " and " + str(dir_files[i]) + " are duplicated by content"))
    return duplicates


# print_duplicates('dz')
# print_duplicates('dz')

### Task 4.5
def memoize(function):
    memo = {}

    def wrapper(*args):
        if len(memo) > 0:
            return memo[0]
        else:
            result = function(*args)
            memo[0] = result
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
print(set_pixel((0, 127, 250)))
