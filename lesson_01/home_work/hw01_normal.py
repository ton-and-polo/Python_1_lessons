
__author__ = "Iaroslav Marushchak"

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Число приходит в виде целого беззнакового.


# Задача-2: Запросить у пользователя два целых числа, связать их с переменными.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math

# 1st part:
user_input = input("Enter number:\n")
print("Max int: ", max(user_input))

# 2nd part:
first = int(input("Enter number:\n"))
second = int(input("Enter another number:\n"))
first, second = second, first
print(first, second)

# 3rd part:
print("ax2 + bx - c = 0")
a = int(input("Enter 'a':\n"))
b = int(input("Enter 'b':\n"))
c = int(input("Enter 'c':\n"))
d = (b * b) - (4 * a * c) # discriminant
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = ", x1, "\nx2 = ", x2)
elif d == 0:
    x = -b / 2 * a
    print("x = ", x)
else:
    print("Your function has no real roots.")