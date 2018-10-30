# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь. Вывести результат
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# 1
print("1st part:")
import cmath

x = [2, -5, 8, 9, -25, 25, 4]
new_x = []
counter = 0
for i in x:
    i = str(cmath.sqrt(i))
    if len(i) == 6: # e.g (3+0j) contains 6 char
        i = int(i[1:2])
        new_x.append(i)
    counter += 1
print(new_x)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# 2
print("2nd part:")
date = input("Enter date (dd.mm.yyyy):\n")

days = {
    "01":"1st",
    "02":"2nd",
    "03":"3rd",
    "04":"4th",
    "05":"5th",
    "06":"6th",
    "07":"7th",
    "08":"8th",
    "09":"9th",
    "10":"10th",
    "11":"11st",
    "12":"12nd",
    "13":"13rd",
    "14":"14th",
    "15":"15th",
    "16":"16th",
    "17":"17th",
    "18":"18th",
    "19":"19th",
    "20":"20th",
    "21":"21st",
    "22":"22nd",
    "23":"23rd",
    "24":"24th",
    "25":"25th",
    "26":"26th",
    "27":"27th",
    "28":"28th",
    "29":"29th",
    "30":"30th",
    "31":"31st"
}

months = {
    "01":"January",
    "02":"February",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}

day = "" # day - date[0:2]
month = "" # month - date[3:5]
year = date[6:10] # didn't add dict for this variable (think it's redundant)

for key, value in days.items():
    if key == date[0:2]:
        day += value

for key, value in months.items():
    if key == date[3:5]:
        month += value

print("{} {},".format(month, day), year)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
# выведите созданный список

# 3
print("3rd part:")
import random
my_list = []
my_list_length = random.randint(1, 10) # 1 <= my_list_length <= 10
i = 0
while i < my_list_length:
    my_list.append(random.randint(-100, 100))
    i += 1
print(my_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
# выведите результаты

# 4
print("4th part:")
# a)
print("a)")
lst_a = [1, 2, 4, 5, 6, 2, 5, 2]
lst_a.sort()
for i in lst_a:
    if lst_a.count(i) > 1:
       lst_a.remove(i)
lst_a2 = lst_a.copy()
print(lst_a2)

# b)
print("b)")
lst_b = [1, 2, 4, 5, 6, 2, 5, 2]
lst_b2 =[]
for i in lst_b:
    if lst_b.count(i) == 1:
        lst_b2.append(i)
print(lst_b2)
