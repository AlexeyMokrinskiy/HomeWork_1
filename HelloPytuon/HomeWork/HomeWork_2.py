'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
*Пример:*
- 6782 -> 23
- 0.56 -> 11
'''

# my_number = str(input('Введите число: '))
# sum_of_digits = 0

# for i in my_number:
#     if i.isdigit():
#         sum_of_digits += int(i)

# print(my_number, '->', sum_of_digits)

'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

# num_n = int(input('Введите N: '))
# factorial = 1

# print('пусть N =', num_n,', тогда [', end='')
# for i in range (num_n):
#     factorial *= i+1
#     print(factorial, end=', ')

# print(']')

'''
3. Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
*Пример:*
- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072 
'''

# num_n = int(input('Введите n: '))
# print('Для n =', num_n, end=': [')
# sum = 0

# for i in range(1, num_n + 1):
#     i = round(((1 + 1 / i)**i), 2)
#     print(i, end=', ')
#     sum += i

# print('] -> ', sum)

'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
'''
# num_element = int(input('Введите элементы N: '))
# numbers = []

# for i in range(-num_element, num_element+1):
#     numbers.append(i)

# print(numbers)

# first_position = int(input('Введите первую позицию элемента: '))
# print(numbers[first_position])

# second_position = int(input('Введите вторую позицию элемента: '))
# print(numbers[second_position])

# mult_position = numbers[first_position] * numbers[second_position]

# print(f'произведением позиции {first_position} и позиции {second_position} будет {mult_position}')

'''
5. Реализуйте алгоритм перемешивания списка.
'''

# from random import Random, randint

# size = int(input('Введите размер списка '))
# min_value = int(input('Введите минимальное значение '))
# max_value = int(input('Введите максимальное значение '))

# first_list = []
# for i in range(size):
#     first_list.append(randint(min_value, max_value))
# print('первый список       ->',first_list)

# second_list = first_list[:]
# for i in range(size):
#     index = randint(0, size - 1)
#     temp = second_list[i]
#     second_list[i] = second_list[index]
#     second_list[index] = temp
# print('перемешанный список ->',second_list)