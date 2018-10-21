# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
#
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# подсказка: x у вас уже есть, остается с помощью срезов получить значения k и b,
# а затем вевести итоговый результат: print('y = {}'.format(k * x + b))

# 1
print("1st part:")
# y = kx + b
equation = "y = -12x + 11111140.2121"
x = 2.5
# equation = (-12 * 2.5) = -30 + 11111140.2121"
k = int(equation[4:7])
b = float(equation[-13:])
print("y = {}".format(k * x + b))


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:

# 1. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа (числа) для дня, 2 - для месяца, 4 - для года)

# 2. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 3. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 4. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999

# 2
print("2nd part:")
date = input("Enter date (dd.mm.yyyy):\n")

date_list = date.split(".")

date_length = 0 # initial value
for i in date_list:
    date_length += len(i)

correct_date_length= 8
max_day = 31
max_month = 12
max_year = 9999

day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])

if date_length != correct_date_length:
    print("Invalid date format")
elif max_day < day or day < 0:
    print("Invalid day")
elif max_month < month or month < 0:
    print("Invalid month")
elif max_year < year or max_year < 0:
    print("Invalid year")
else:
    print("Correct date format")