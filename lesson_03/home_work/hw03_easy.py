# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# 1:
print("1st part:")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# 2:
print("2nd part:")

def lucky_ticket(number):
    number = str(number)
    result = ""
    def sum(lst):
        result = 0
        for i in lst:
            result += int(i)
        return result
    left_part_sum = sum(number[:3])
    right_part_sum = sum(number[3:])
    if left_part_sum == right_part_sum:
        result = True
    else:
        result = False
    return result

print(lucky_ticket(590185)) # True
print(lucky_ticket(998001)) # False




