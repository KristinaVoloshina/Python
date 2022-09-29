# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day=int(input('Введите число '))
if day>7 or day<1:
    print('Проверьте введенное число.')
elif day==6 or day==7:
    print('Это выходной!')
else:
    print('Это будний день.')

# 2.Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
a = x * y * z
b = x + y + z
if a > 0:
   a = 0
elif a < 1:
   a = 1
if b > 0:
   b = 1
elif b < 1:
   b = 1
if a == b:
   print('Правда')
elif a != b:
   print('Ложь')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')
   

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Проверьте введенное число')
elif n == 1:
    print('x > 0 and y > 0')
elif n == 2:
    print('x < 0 and y > 0')
elif n == 3:
    print('x < 0 and y < 0')
elif n == 4:
    print('x > 0 and y < 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


print('Enter coordinates point А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Enter coordinates point B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) # Теорема Пифагора 