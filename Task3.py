# 3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check(x, y):
    if x.isdigit() and y.isdigit():
        return True
    else:
        try:
            float(x)
            float(y)
            return True
        except ValueError:
            return False


def coordinat(x, y):
    if float(x) == 0 and float(y) == 0:
        a = "в начале координат"
    elif float(x) == 0 and float(y) != 0:
        a = "на оси y"
    elif float(x) != 0 and float(y) == 0:
        a = "на оси x"
    elif float(x) > 0 and float(y) > 0:
        a = "в I четверти плоскости"
    elif float(x) < 0 and float(y) > 0:
        a = "в II четверти плоскости"
    elif float(x) < 0 and float(y) < 0:
        a = "в III четверти плоскости"
    elif float(x) > 0 and float(y) < 0:
        a = "в IV четверти плоскости"
    print(f"Точка с координатами {x}, {y} находится {a}. ")


x = input('Введите координату Х: ')
y = input('Введите координату Y: ')

while True:
    if check(x, y) == False:
        print('НЕ ВЕРНЫЙ ВВОД. ПОВТОРИТЕ ПОПЫТКУ ЕЩЕ')
        x = input('Введите координату Х: ')
        y = input('Введите координату Y: ')
    else:
        coordinat(x, y)
        break
