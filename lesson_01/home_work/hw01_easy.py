
__author__ = "Iaroslav Marushchak"

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа


# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


# 1st part:
user_input = input("Enter number:\n")
list(user_input)
for i in user_input:
    print(i)

# 2nd part:
a = int(input("Enter number:\n"))
b = int(input("Enter another number:\n"))
a, b = b, a
print(a, b)

# 3rd part:
age_limit = "18"
user_age = input("Enter your age:\n")
if user_age >= age_limit:
    print("Access allowed")
else:
    print("Access denied. You're under", age_limit)