#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11

#num = input('Введите число: ')
#sum = 0
#for i in num:
#    if i!= ",":
 #       sum = sum + int(i)
#print(f"Сума {num} равна: ", sum)

num = input('Введите вещественное число: ')
sum = sum(map(int, num.replace('.', '')))
print (sum)

#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих
# на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#def Odd_sum(list):
#    sum = 0
#    for i in range(len(list)):
#        if i % 2 !=0:
#            sum+=list[i]
#    return sum
#list = [2, 3, 5, 9, 3]

#sum_num = Odd_sum(list)

#print(f'Сумма чисел на нечетных позициях 3 и 9, ответ: {sum_num}')

my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))

# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

#def mult_lst(lst):
#    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#    print(new_lst)

#lst = [2, 3, 4, 5, 6]
#mult_lst(lst)
#lst = list(map(int, input("Введите числа через пробел:\n").split()))
#mult_lst(lst)

import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3, 6); B (2, 1) -> 5,09
#- A (7, -5); B (1, -1) -> 7,21


#def input_numbers(x): 
#    xy = ["X", "Y"]
#    a = []
#    for i in range(x):
#        reality = False
#        while not reality:
#            try:
#                number = int(input(f'Введите координату {xy[i]}: '))
#                a.append(number)
#                reality = True
#            except ValueError:
#                print('Введите 1 цифра до запятой, 2 после запятой')
#    return a


#def Length(a, b):  
#    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)  
#   return lengthSegment


#print('Введите координаты точки А')
#pointA = input_numbers(2)
#print('Введите координаты точки В')
#pointB = input_numbers(2)

#print(f'Длина отрезка: {round(Length(pointA, pointB),2)}')

from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(dot_range(dot_1, dot_2))

