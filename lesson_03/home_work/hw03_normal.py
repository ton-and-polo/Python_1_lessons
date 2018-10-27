# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# 3:
print("3rd part:")

my_list = [-10, 2, 66, 7, 3, 0, 66]

def bubble_sort(lst):
    counter = 1
    while counter < len(lst):
         for i in range(len(lst) - counter): # - counter: not compare sorted i
              if lst[i] > lst[i+1]:
                  lst[i], lst[i+1] = lst[i+1], lst[i]
         counter += 1
    return lst

print(bubble_sort(my_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

