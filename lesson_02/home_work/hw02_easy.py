# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# 1
print("1st part:")
fruit_list = ["apple", "banana", "kiwi", "watermelon"]
index = 1 # initial value
for i in fruit_list:
    print("{}.{}".format(index, i))
    index += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.

# 2
print("2nd part:")
x = [1, 2, 3, 12, 8, 93] # arbitrary list
y = [1, 5, 3, 8] # another arbitrary list
i = 0
for element in x:
    if x[i] == y[i]:
        x.pop(i)
    i += 1
print(x)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

# 3
print("3rd part:")
arbitrary_list = [2, 3, 12, 8, 93]
new_arbitrary_list = []
for i in arbitrary_list:
    if i % 2 == 0:
        i /= 4
        new_arbitrary_list.append(i)
    else:
        i *= 2
        new_arbitrary_list.append(i)
print(new_arbitrary_list)