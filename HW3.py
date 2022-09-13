# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = int(input('Input size of a list: '))
def random_list(n):
    '''Создаем список из рандомных целых чисел'''
    spisok = []
    for i in range(0, n):
        i = randint(1,10)
        spisok.append(i)
    return spisok
spisok1 = random_list(n)
print(spisok1)
def sum_odd_position(spisok):
    '''Функция возвращает сумму элементов списка, стоящих на нечётной позиции'''
    sum = 0
    for i in range(1, len(spisok), 2):
        sum += spisok[i]
    return sum
sum1 = sum_odd_position(spisok1)
print(f'The sum of element on odd positions is: {sum1}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
from random import randint

while True:
    try: 
        num2 = int(input('Input size of a list: '))
        break
    except: 
        print('invalid input!')
def create_list(n):
    '''Создаем список из рандомных целых чисел'''
    l = []
    for i in range(0, n):
        i = randint(0, 10)
        l.append(i)
    return l
spisok2 = create_list(num2)
print(f'Initial list: {spisok2}')
def mult_couple(spisok):
    '''Функция возвращает список произведений пар чисел'''
    spisok_reversed = spisok[::-1]
    spisok_mult_couple = []
    for i in range(0, math.ceil(len(spisok)/2)):
        i = spisok[i] * spisok_reversed[i]
        spisok_mult_couple.append(i)
    return spisok_mult_couple
spisok_mult_couple = mult_couple(spisok2)
print(f'List of mutiplied couples: {spisok_mult_couple}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from random import randint, random

while True:
    try:
        num3 = int(input('Input size of a list: '))
        break
    except:
        print('Invalid input')
def create_list2(n):
    '''Создаем список рагдомных вещественных чисел'''
    spisok = []
    for i in range(0, n):
        i = round((randint(0, 20) + random()), 4)
        spisok.append(i)
    return spisok
spisok3 = create_list2(num3)
print(spisok3)
def difference_fractional_part(spisok):
    '''Находим разницу между минимальной и максимальной дробной частью'''
    dif = 0
    min = round(spisok[0] - int(spisok[0]), 4)
    max = round(spisok[0] - int(spisok[0]), 4)
    for i in spisok[1:]:
        i = round(i - int(i), 4)
        if min > i:
            min = i
        if max < i:
            max = i
    dif = round(max - min, 4)
    return min, max, dif
difference = difference_fractional_part(spisok3)
print(f'Difference between max = {difference[1]} and min = {difference[0]} fractional parts of elements is: {difference[2]}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

while True:
    try:
        num4 = int(input("Input a number: "))
        break
    except:
        print('Invalid input!')
def number_conversion(n):
    '''Функция переводит десятичное число в двоичное'''
    div = ''
    while n != 0:
        div = str(n % 2) + div
        n = n // 2
    div = int(div)
    return div
print(f'{num4} in binary: {number_conversion(num4)}')
div = ''
def number_conversion_recursion(n, div):
    '''Функция переводит десятичное число в двоичное с помощью рекурсии'''
    while n != 0:
        div = str(n % 2) + div
        return number_conversion_recursion(n//2, div)
    div = int(div)
    return div
print(f'{num4} in binary using the recursion: {number_conversion_recursion(num4, div)}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

while True:
    try:
        num5 = int(input('Input a number: '))
        break
    except:
        print('Invalid input!')
def create_list5(n):
    '''Функция создает список из n элементов'''
    spisok = []
    for i in range(n):
        spisok.append(0)
    return spisok
list1 = create_list5(num5 + 1)
list2 = create_list5(num5)
def non_fibonacci(spisok1, spisok2):
    '''Функция возвращает список Негафибоначчи'''
    for i in range(len(spisok1)):
        if i == 0 or i == 1:
            spisok1[i] = i
        else: 
            spisok1[i] = spisok1[i - 2] + spisok1[i - 1]
    for i in range(len(spisok2)):
        if i == 0 or i == 1:
            spisok2[i] = (-1)**i
        else:
            spisok2[i] = spisok2[i - 2] - spisok2[i -1]
    spisok2.reverse()
    spisok2.extend(spisok1)
    return spisok2
print(f'List of non Fibonacci numbers: {non_fibonacci(list1, list2)}')