# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# WeekDay = int(input('введите день недели: '))
# if WeekDay < 1 or WeekDay > 7:
#     print('введено неверное значение')
# elif WeekDay >= 1 and WeekDay < 6:
#     print(WeekDay,'-> нет')
# else: 
#     print(WeekDay,'-> да')

#______________________________________________________________________________________

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for X in range(2):
#     for Y in range(2):
#         for Z in range(2):
#             print(X,'AND',Y,'OR',Z,'=',X and Y or Z)

#______________________________________________________________________________________

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# X = int(input('введите точку Х: '))
# Y = int(input('введите точку Y: '))
# if X > 0 and Y > 0:
#     print('x =', X,'; y =', Y, '-> 1')
# elif X < 0 and Y > 0:
#     print('x =', X,'; y =', Y, '-> 2')
# elif X < 0 and Y < 0:
#     print('x =', X,'; y =', Y, '-> 3')
# elif X > 0 and Y < 0:
#     print('x =', X,'; y =', Y, '-> 4')
# elif X == 0:
#     print('точка лежит на оси Х')
# elif Y == 0:
#     print('точка лежит на оси Y')

#_______________________________________________________________________________________________________________

# 3. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# QuarterCoordinates = int(input('введите четверть координат: '))
# if QuarterCoordinates == 1:
#     print('диапазон возможных координат точек в этой четверти:\n 0 < x < +oo\n 0 < y < +oo')
# elif QuarterCoordinates == 2:
#     print('диапазон возможных координат точек в этой четверти:\n 0 < x < -oo\n 0 < y < +oo')
# elif QuarterCoordinates == 3:
#     print('диапазон возможных координат точек в этой четверти:\n 0 < x < -oo\n 0 < y < -oo')
# elif QuarterCoordinates == 4:
#     print('диапазон возможных координат точек в этой четверти:\n 0 < x < +oo\n 0 < y < -oo')
# else:
#     print('введено неверное значение')

#__________________________________________________________________________________________________________________

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Xa = int(input('введите координаты точки А по оси Х: '))
# Ya = int(input('введите координаты точки А по оси У: '))
# Xb = int(input('введите координаты точки В по оси Х: '))
# Yb = int(input('введите координаты точки В по оси У: '))
# Z = float((Xa - Xb)**2 + (Ya - Yb)**2) ** 0.5
# print('->', round(Z, 3))
# print('A', (Xa,Ya),'; B', (Xb,Yb), '->',round(Z, 3))