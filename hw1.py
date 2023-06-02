# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# # наприклад:
# # st = 'as 23 fdfdg544' # введена строка
# # 2,3,5,4,4        #вивело в консолі.
#
# st = input('Enter line:\n')
# li = ', '.join([i for i in st if i.isdigit()])
# print(li)
#
# # #################################################################################
#
# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # так як вони написані
# # наприклад:
# # st = 'as 23 fdfdg544 34' #введена строка
# #   23, 544, 34              #вивело в консолі
#
# st = input('Enter line:\n')
# li = ', '.join(''.join([i if i.isdigit() else ' ' for i in st]).split())
# print(li)
#
# # #################################################################################
#
# # list comprehension
# #
# # 1)є строка:
# greeting = 'Hello, world'
# # записати кожний символ як окремий елемент списку і зробити його заглавним:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# li = [i.upper() for i in greeting]
# print(li)
#
# # #################################################################################
#
# # 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# # приклад:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# li = [i**2 for i in range(0, 50) if i % 2]
# print(li)
#
# # #################################################################################
from typing import List

# # function
#
# - створити функцію яка виводить ліст
# li = [3, 5, 7, 1, 4, 3]
#
#
# def printer(l):
#     print(l)
#
#
# printer(li)
#
# # #################################################################################
# # - створити функцію яка приймає три числа та виводить та повертає найбільше.
#
# def max_of_entered(a, b, c):
#     m = max(a, b, c)
#     print(f'Entered numbers: {a}, {b}, {c}\nMax number out of entered {m}')
#     return m
#
#
# max_of_entered(1, 0, 2)
#
# # - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
#
# def max_and_min(*args):
#     max_number = max(args)
#     min_number = min(args)
#     print(f'Entered numbers: {args}\nMax number is {max_number}')
#     return min_number
#
#
# print(f'Min number is: {max_and_min(3, 5, 1, 5, 7, 9, 0, -5, 6)}')
#
# # #################################################################################
# # - створити функцію яка повертає найбільше число з ліста
#
# li = [2, 7, 0, -3, 6, -10, 23]
#
#
# def max_in_list(l):
#     return max(l)
#
#
# print(f'Max number in list: {max_in_list(li)}')
#
# # #################################################################################
# # - створити функцію яка повертає найменьше число з ліста
#
# li = [2, 7, 0, -3, 6, -10, 23]
#
#
# def min_in_list(l):
#     return min(l)
#
#
# print(f'Min number in list: {min_in_list(li)}')
#
# # #################################################################################
# # - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
#
# li = [2, 7, 0, -3, 6, -10, 23]
#
#
# def sum_of_list(l):
#     return sum(l)
#
#
# print(f'Sum of list: {sum_of_list(li)}')
#
# # #################################################################################
# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
# li = [2, 7, 0, -3, 6, -10, 23]
#
#
# def avg_of_list(l):
#     return sum(l) / len(l)
#
#
# print(f'Average of list: {avg_of_list(li)}')
#
# ################################################################################################
# 1)Дан list:
# #
# lists = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
#
#
# #
# # #   - знайти мін число
# #
# def min_number(li):
#     return min(li)
#
#
#
#
# # print(f'Min number in list: {min_number(list)}')
# #
# # #   - видалити усі дублікати
# #
#
#
# def without_duplicates(li):
#     list_without_duplicates = li.copy()
#     return set(list_without_duplicates)
#
#
#
#
# # print(f'List without duplicates: {without_duplicates(list_without_duplicates)}')
# #
# # #   - замінити кожне 4-те значення на 'X'
#
#
#
# def changer(li):
#     x_list = li.copy()
#     for i in range(3, len(x_list), 4):
#         x_list[i] = 'X'
#     return x_list
#
#
#
#
# #
# #
# # print(f'List with changed every 4th value to "X": {changer(x_list)}')
# #
# # # 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# #
# def square(size):
#     for i in range(1, size + 1):
#         if i == 1 or i == size:
#             print('* ' * size)
#         else:
#             print('*' + ' ' * 2 * (size - 2) + ' ' + '*')
#
#
#
#
# #
# # square(7)
# #
# # # 3) вывести табличку множення за допомогою цикла while
# #
# def multiplication_table():
#     column = 1
#     while column in range(11):
#         row = 1
#         while row in range(11):
#             print(f'{(column * row):3}', end=' ')
#             row += 1
#         print()
#         column += 1
#
#
#
#
# #
# #
# # multiplication_table()
# #
# # 4) переробити це завдання під меню
# #
# while True:
#     print('1. Find the min number\n'
#           '2. Remove duplicates\n'
#           "3. Change every 4th value to 'X'\n"
#           '4. Print a square\n'
#           '5. Multiplication table\n'
#           '6. Exit\n')
#
#     choice = int(input('Enter your choice: '))
#     print()
#
#     if choice == 1:
#         print(f'Min number in list: {min_number(lists)}\n')
#     elif choice == 2:
#         print(f'List without duplicates: {without_duplicates(lists)}\n')
#     elif choice == 3:
#         print(f'List with changed every 4th value to "X": {changer(lists)}\n')
#     elif choice == 4:
#         a = int(input('Enter the square size: '))
#         print('\n\tSquare: \n')
#         square(a)
#         print('\n')
#     elif choice == 5:
#         print('\tMultiplication table:\n')
#         multiplication_table()
#         print('\n')
#     elif choice == 6:
#         break
