'''
1. Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

# from random import Random, randint

# size = int(input('Введите размер списка '))
# min_value = int(input('Введите минимальное значение '))
# max_value = int(input('Введите максимальное значение '))

# random_list = []
# for i in range(size):
#     random_list.append(randint(min_value, max_value))
# print('Наш список', random_list)

# odd_list = random_list[1::2]
# print('Hа нечётных позициях элементы', odd_list)

# sum = 0
# for i in range(len(odd_list)):
#     sum += odd_list[i]
# print('Oтвет:', sum)

'''
2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# from random import Random, randint

# size = int(input('Введите размер списка '))
# min_value = int(input('Введите минимальное значение '))
# max_value = int(input('Введите максимальное значение '))

# random_list = []
# for i in range(size):
#     random_list.append(randint(min_value, max_value))
# print(random_list, '=>', end=' ')

# new_list = []
# for i in range(len(random_list)):
#     while i < len(random_list) / 2 and size > len(random_list) / 2:
#         size = size - 1
#         j = random_list[i] * random_list[size]
#         new_list.append(j)
#         i +=1

# print(new_list)

'''
3. Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

# from random import Random, uniform

# size = int(input('Введите размер списка '))
# min_value = float(input('Введите минимальное значение '))
# max_value = float(input('Введите максимальное значение '))

# random_list = []
# for i in range(size):
#     random_list.append(uniform(min_value, max_value)) # не разобрался с округлением(

# print(random_list, end=' => ')
# print(max(random_list) - min(random_list)) # c функцией мах
# random_list.sort()                         # с функцией sort
# print(random_list[-1] - random_list[0])

# def Diff(arr):                             # или перебором
#     max_ = arr[0]
#     min_ = arr[0]
#     for ele in arr:
#         if ele > max_:
#            max_ = ele
#         elif ele < min_:
#             min = ele
#     return max_ - min_

# result = Diff(random_list)
# print(result)

'''
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

# my_number = int(input('Введите число: '))

# binar_number = ""
# while my_number > 0:
#     binar_number = str(my_number % 2) + binar_number
#     my_number //= 2

# print(f'Результат перевода в двоичную систему ->', {binar_number})

'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

# my_number = int(input('Введите число: '))

# fibonnacci = []
# nego_fibonacci = []

# a, b = 1, 0
# c, d = 1, 0

# for i in range(my_number+1):
#         a, b = b, a + b
#         fibonnacci.append(a)
# fibonnacci = fibonnacci[1:]

# for i in range(-my_number-1, 0):
#         c, d = d, c - d
#         nego_fibonacci.append(c)
# nego_fibonacci = nego_fibonacci[::-1]   

# print(f'для k = {my_number} список будет выглядеть так:', nego_fibonacci + fibonnacci)