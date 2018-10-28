# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# 1:
print("1st part:")

def fibonacci_sequence(start, stop): # Fn = F(n-1) + F(n-2)
    a = 0
    b = 1
    # evaluate fibonacci till start point:
    for _ in range(start - 1):
        a, b = b, a + b
    # evaluate fibonacci till stop point:
    index = start
    while index <= stop:
        a, b = b, a + b
        print("f{}:{}".format(index, a))
        index += 1

print(fibonacci_sequence(4, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# 2:
print("2rd part:")

my_list = [-10, 2, 66, 7, 3, 0, 66]

def bubble_sort(lst):
    counter = 1
    while counter < len(lst):
         for i in range(len(lst) - counter):
              if lst[i] > lst[i+1]:
                  lst[i], lst[i+1] = lst[i+1], lst[i]
         counter += 1
    return lst

print(bubble_sort(my_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# 3:
print("3rd part:")

# first my_filter() argument (function):
def my_func(x):
  if x < 18:
    return False
  else:
    return True

# second my_filter() argument (iterable):
ages = [5, 12, 17, 18, 24, 32]

def my_filter(function, iterable):
    result =[]
    for i in iterable:
        if function(i):
            result.append(i)

    return result


adults = my_filter(my_func, ages)
print(adults)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# 4:
print("4th part:")
import math

figure = [
    [2, 2], # A
    [4, 6], # B
    [12, 6], # C
    [10, 2] # D
]

def is_parallelogram(figure):

    # sub_func to evaluate side length:
    def side_length(p1, p2):
        # x = V(x2-x1)2 + (y2-y1)2 (V - square root sign, 2 - in power of 2)
        length = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        return length

    AB = side_length(figure[0], figure[1])
    BC = side_length(figure[1], figure[2])
    CD = side_length(figure[2], figure[3])
    DA = side_length(figure[3], figure[0])

    if AB == CD and BC == DA:
        return True
    else:
        return False


print(is_parallelogram(figure))