# 5-Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def check_num():
    while True:
        try:
            num = float(input('Enter number: '))
            return num
        except ValueError:
            print('Error! Try again.')


def get_dis():
    print('Enter X point A')
    point_ax = check_num()
    print()
    print('Enter Y point A')
    point_ay = check_num()
    print()
    print('Enter X point B')
    point_bx = check_num()
    print()
    print('Enter Y point B')
    point_by = check_num()
    delta_x = point_ax - point_bx
    delta_y = point_ay - point_by
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
    # distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
    print(f'Distance between A и B is: {distance:.4f}')


get_dis()
