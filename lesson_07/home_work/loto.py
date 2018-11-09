#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random



def bubble_sort(lst):
    counter = 1
    while counter < len(lst):
         for i in range(len(lst) - counter):
              if lst[i] > lst[i+1]:
                  lst[i], lst[i+1] = lst[i+1], lst[i]
         counter += 1
    return lst

def bingo_line():
    # make initial list with 9 items (0)
    bingo_line = []
    for i in range(9):
        bingo_line.append("-")

    # make list with 5 random numbers (1-90)
    # and sort them from lower to upper
    random_list = []
    for i in range(5):
        random_list.append(random.randint(1, 90))
    bubble_sort(random_list)

    # make list with 5 random index (0-4)
    # and sort them from lower to upper
    random_index = []
    i = 0
    while i < 5:
        el = random.randint(0, 8)
        if el not in random_index:
            random_index.append(el)
            i += 1
    bubble_sort(random_index)

    # result - 9 items in line
    # 5 full(rand_num) with random numbers (0 < num < 91)
    # and 4 empty("-")
    for i in range(5):
        index = random_index[i]
        number = random_list[i]
        bingo_line[index] = number

    return bingo_line

def bingo_card():
    bingo_card = []
    for i in range(3):
        card_line = bingo_line()
        bingo_card.append(card_line)

    return bingo_card

def selected_numbers():
    selected_numbers = []
    selected_i = 0
    while selected_i < 90:
        el = random.randint(1, 90)
        if el not in selected_numbers:
            selected_numbers.append(el)
            selected_i += 1
    return selected_numbers

def bingo(lst):
    result = False
    x_list = []
    for line in lst:
        for i in line:
            if i == "x":
                x_list.append(i)
        if len(x_list) < 5:
            x_list = []
        elif len(x_list) == 5:
            result = True
            break

    return result

# Bingo game:

user_card = bingo_card()
computer_card = bingo_card()
selected_numbers = selected_numbers()
move = 1
all_moves = 90

for i in range(90):
    numbers_left = all_moves - move
    selected_number = selected_numbers[move - 1]
    print("Selected number \"{}\" (numbers lef: {})".format(selected_number, numbers_left))

    print("Computer card:")
    for i in computer_card:
        print(i)

    print("Your card:")
    for i in user_card:
        print(i)

    user_input = input("Mark selected number (y/n)? ")

    def is_num_on_card(lst, number):
        result = False
        for i in lst:
            for el in i:
                if el == number:
                    result = True
        return result


    def mark_number(lst, number):
        l_index = 0
        for l in lst:
            el_index = 0
            for el in l:
                if el == number:
                    lst[l_index][el_index] = "x"
                el_index += 1
            l_index += 1

    if user_input == "y":
        if is_num_on_card(user_card, selected_number):
            mark_number(user_card, selected_number)
        else:
            print("You lost!")
            break
    elif user_input == "n":
        if is_num_on_card(user_card, selected_number):
            print("You lost!")
            break

    mark_number(computer_card, selected_number)

    if bingo(user_card):
        print("User - BINGO!")
        break

    if bingo(computer_card):
        print("Computer - BINGO!")
        break

    move += 1
