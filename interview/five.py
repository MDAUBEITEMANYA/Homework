### Task 5.2
class Bird:
    name = ""

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name + "can fly")

    def walk(self):
        print(self.name + " bird can walk")


# b = Bird("Any")
# b.walk()


# class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
class FlyingBird(Bird):
    ration = "worms"

    def __init__(self, name, ration):
        self.name = name
        self.ration = ration

    def eat(self):
        print("I'm eating " + str(self.ration))

    def __str__(self):
        return self.name + " can walk and fly"


class NonFlyingBird(Bird):
    ration = "fish"

    def __init__(self, name, ration):
        self.name = name
        self.ration = ration

    def eat(self):
        print(self.name + "Is eating " + str(self.ration) + " cause it likes fish!")

    def swim(self):
        print(self.name + " can swim")

    def fly(self):
        raise AttributeError(self.name + " - NonFlyingBird object has no attribute 'fly'")

    def __str__(self):
        return self.name + " can walk"


class SuperBird(NonFlyingBird, FlyingBird):

    def __init__(self, name, ration):
        self.name = name
        self.ration = ration

    def eat(self):
        print(self.name + " is eating" + str(self.ration) + " cause It can eat everything")

    def fly(self):
        print(self.name + " can fly")

    def __str__(self):
        return self.name + " can walk, swim and fly"


superBird = SuperBird("duck", "bread")


# superBird.eat()
# superBird.fly()
# print(str(superBird))


### Task 5.3
# not lazy
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


singleton = Singleton()
# print("Obj created", singleton)
singleton1 = Singleton()

# print("Object created", singleton1)
# print(singleton1 is singleton)

import random

### Task 5.4

import numpy as np
import random


class Matrix:

    def __init__(self, *args):
        if len(args) < 1:
            self.array = []
            return

        if isinstance(args[0], list):
            self.create_matrix(args)
        else:
            self.generate_matrix(args)

    def generate_matrix(self, args):
        self.rows = args[0]
        self.cols = args[1]
        self.array = np.random.randint(10, size=(2, 3))

    def create_matrix(self, args):
        self.rows = len(args)
        self.cols = len(args[0])
        self.array = args

    def __add__(self, matrix):
        tmp = Matrix()
        if self.cols == matrix.cols and self.rows == matrix.rows:
            for i in range(len(self.array)):
                tmp_list = []
                for j in range(len(self.array[0])):
                    tmp_list.append(self.array[i][j] + matrix.array[i][j])
                tmp.array.append(tmp_list)
            return tmp
        else:
            raise ArithmeticError("Матрицы разного размера")

    def __subtract__(self, matrix):
        tmp = Matrix()
        if self.cols == matrix.cols and self.rows == matrix.rows:
            for i in range(len(self.array)):
                tmp_list = []
                for j in range(len(self.array[0])):
                    tmp_list.append(self.array[i][j] - matrix.array[i][j])
                tmp.array.append(tmp_list)
            return tmp
        else:
            raise ArithmeticError("Матрицы разного размера")

    def __scalar_multiplication__(self, number: int):
        tmp = Matrix()
        for i in range(len(self.array)):
            tmp_list = []
            for j in range(len(self.array[0])):
                tmp_list.append(self.array[i][j] * number)
            tmp.array.append(tmp_list)
        return tmp

    def __str__(self):
        return str(self.array)

    def transpose(self):
        rez = []
        for row in self.array:
            print(row)
            rez = [[self.array[j][i] for j in range(len(self.array))] for i in range(len(self.array[0]))]
            print("\n")
        return rez

    def is_equal(self, matrix):
        if self.cols != matrix.cols and self.rows != matrix.rows:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] != matrix.array[i][j]:
                    return False
        return True

    def is_squared(self):
        return self.rows == self.cols


matrix = Matrix(3, 2)
matrix2 = Matrix(3, 3)
print("____________________________")
print(matrix.is_squared())
print(matrix2.is_squared())
#matrix1 = Matrix([1, 2], [3, 4])
#matrix4 = Matrix([1, 2], [3, 4])
#matrix5 = Matrix([1, 2], [3, 0])
#print(matrix4.is_equal(matrix1))
#print(matrix4.is_equal(matrix5))
# matrix4 = Matrix([1,2],[3,4],[5,6])
# print(matrix4)
# matrix4.transpose()
print("______________________________")
# print(matrix2)
print("______________________________")


# print(matrix2.__add__(matrix))
# print(matrix2.__subtract__(matrix))
# print(matrix.__scalar_multiplication__(2))


class Summa:

    def __init__(self):
        self._my_sum = ""

    @property
    def my_sum(self):
        return self._my_sum

    # Setter method
    @my_sum.setter
    def name(self, val):
        if val != "":
            self._my_sum = val
        else:
            print("You can't do it")


# s = Summa()
# print(s.name)
# s.name = "mosha"
# print(s.name)
# s.name = ""
# print(s.name)

### Task 5.1

class HistoryDict:
    dictionary = {}
    history = []

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def in_dictionary(self, key):
        return key in dict(self.dictionary)

    def set_value(self, key, value):
        self.history.append(key)
        if len(self.history) > 9:
            for x in range(9):
                self.history[x - 1] = self.history[x]
        self.dictionary[key] = value

    def get_history(self):
        print(self.history)

# d = HistoryDict({"foo": 42})
# d.set_value("bar", 43)
# d.get_history()
