
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
user_input_list = []
for i in user_input:
    user_input_list.append(int(i))
print("Max int: ", max(user_input_list))

# 2nd part:
a = int(input("Enter number:\n"))
b = int(input("Enter another number:\n"))
a, b = b, a
print(a, b)

# 3rd part:
a = 1 # a <= 0
b = 3
c = -4
print("x2 + 3x - 4 = 0")
x1 = int(((-b) + math.sqrt(b * b - 4 * a * c)) / (2 * a))
x2 = int(((-b) - math.sqrt(b * b - 4 * a * c)) / (2 * a))
print("x1 = ", x1, "\nx2 = ", x2)