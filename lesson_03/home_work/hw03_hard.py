# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# 2
print("2nd part:")
import os

# paths:
path_workers = os.path.join("data", "workers")
path_hours = os.path.join("data", "hours_of")

# store all lines in file_1_data:
file = open(path_workers, "r", encoding="UTF-8")
file_1_data = file.readlines()

# store all lines in file_2_data:
file = open(path_hours, "r", encoding="UTF-8")
file_2_data = file.readlines()

workers = [] # list dictionary
i = 1
for line in range(len(file_1_data) - 1):
    info = {}
    name, surname, salary, position, rate_hours = file_1_data[i].split()

    info["full_name"] = name + " " + surname
    info["salary"] = int(salary)
    info["position"] = position
    info["rate_hours"] = int(rate_hours)
    info["salary_per_hour"] = int(info["salary"] / info["rate_hours"])
    workers.append(info)
    i += 1


hours_of = [] # list dictionary
i = 1
for line in range(len(file_2_data) - 1):
    info = {}
    name, surname, hours = file_2_data[i].split()
    info["full_name"] = name + " " + surname
    info["hours"] = int(hours)
    hours_of.append(info)
    i += 1

# append real_hours to workers list:
for line in workers:
    for i_hours_of in hours_of:
        if line["full_name"] == i_hours_of["full_name"]:
            line["hours"] = i_hours_of["hours"]
            continue
    # evaluate salary:
    line["result_salary"] = line["salary_per_hour"] * line["hours"]


    print("{} - {} rub.".format(line["full_name"], line["result_salary"]))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
