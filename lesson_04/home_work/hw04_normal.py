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

