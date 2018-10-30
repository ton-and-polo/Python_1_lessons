# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

# 1
print("1st part:")
import re

# with re:
string = "mtMmEZUOmcq"
lower_case = re.findall('([a-z]+)', string)
print(lower_case)

# without re:
def split_by_upper(string):
    result = []
    element = ""
    index = 1

    for i in string:
        if i.islower():
            element += i
        elif i.isupper():
            if len(element) != 0:
                result.append(element)
                element = ""
        index += 1

        if index > len(string):
            result.append(element)
            element = ""

    return result

my_string = "mtMmEZUOmcq"

print(split_by_upper(my_string))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

# 2
print("2nd part:")
import re

# with re:
string = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
pattern = "[a-z]{2}([A-Z]+)[A-Z]{2}"
upper_case = re.findall(pattern, string)
print(upper_case)

# without re:
def split_by_xx_item_XX(string):
    result = []
    lower = ""
    element = ""

    for i in string:
        if i.islower():
            lower += i
            if len(lower) == 3 and len(element) >= 3:
                if element[-3:-1].isupper():
                    element = element[:-2]
                    result.append(element)
                    element = ""
                    lower = lower[2]
            elif len(lower) == 3 and len(element) < 3:
                element = ""
                lower = lower[1:]
        elif i.isupper():
            if len(lower) < 2:
                lower = ""
            elif len(lower) == 2:
                element += i

    return result

my_string = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"

print(split_by_xx_item_XX(my_string))


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

# 3
print("3rd part:")

import os
import re
import random


def sort_item_by_length(lst):
    # Sorting items in the list by its length.
    # The result is list with the biggest item in the end
    counter = 1
    while counter < len(lst):
        for i in range(len(lst) - counter):
            if len(lst[i]) > len(lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        counter += 1
    return lst

def items_same_length(lst):
    # Compare items length in list with last one.
    # If length is equal append this item to new list
    result = []
    for i in lst:
        if len(i) == len(lst[-1]):
            result.append(i)
    return result


# create file
with open("my_file.txt", "w", encoding="UTF-8") as my_file:
    for i in range(2500):
        i = str(random.randint(0, 9))
        my_file.write(i)


# read file
path = os.path.join("my_file.txt")
with open(path, "r", encoding="UTF-8") as my_file:
    for line in my_file:
        patterns = [
            "\d([0]+)",
            "\d([1]+)",
            "\d([2]+)",
            "\d([3]+)",
            "\d([4]+)",
            "\d([5]+)",
            "\d([6]+)",
            "\d([7]+)",
            "\d([8]+)",
            "\d([9]+)",
        ]

        result = []
        for pattern in patterns:
            find = re.findall(pattern, line)
            find = sort_item_by_length(find)
            find = find[-1]
            result.append(find)

        result = sort_item_by_length(result)
        result = items_same_length(result)

        print(result)