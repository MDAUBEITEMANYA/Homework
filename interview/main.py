
def task_two_zero():
    for x in range(1, 100):
        if x % 3 == 0:
            if x % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
                continue
        if x % 5 == 0:
            print("Buzz")
        if (x % 5 != 0) or (x % 3 != 0):
            print(x)


def task_two_one(str):
    counter = 0
    for s in str:
        counter = counter + 1
    return counter


def task_two_two(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def task_two_three():
    items = input("input")
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))


def task_two_four(test_list):
    my_list = list()
    for x in test_list:
        if x < 5:
            my_list.append(x)
    return sorted(set(my_list))


def task_two_five(list_a, list_b):
    a_set = set(list_a)
    b_set = set(list_b)
    print(a_set & b_set)


def task_two_six():
    print('Enter a number')
    number = int(input())
    final_list = [1]
    for x in range(2, number // 2):
        if number % x == 0:
            final_list.append(x)
    final_list.append(number)
    return final_list


def task_two_eight(my_list):
    return set(val for dic in my_list for val in dic.values())


def task_two_nine(numbers):
    result = int(''.join(map(str, numbers)))
    return result


def task_two_ten():
    n = int(input('Enter a positive integer between 1 and 10: '))
    for row in range(1, n + 1):
        print(*("{:3}".format(row * col) for col in range(1, n + 1)))


# Press Ctrl+F8 to toggle the breakpoint.
# task_two_zero()
# print(task_two_one("mosha"))
# print(task_two_two('Oh, it is python'))
# test_list = [1, 11, 2, 4, 7, 8, 234]
# print(task_two_four(test_list))
# task_two_ten()
# numbers = (1, 2, 3)
# print(task_two_nine(numbers))

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
#           {"VIII": "S007"}]
# print(task_two_eight(my_list))

# Task 2.7
#Write a Python program to sort a dictionary by value (descending order).
x = {1: 0, 2: 10, 4: 3, 2: 1, 0: 0}
print(dict(sorted(x.items(), key=lambda item: item[1])))

#reverse
di = {'a':5, 'b':7, 'd':114, 'c':2, 'e':34}
di_sorted = sorted(di , key=di .get, reverse=True)
