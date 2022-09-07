# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

def get_quarter():
    quarter = input('Enter number of quater (from 1 to 4): ')
    while quarter.isdigit() is not True:
        print('Error! Try again.')
        quarter = input('Enter number of quater (from 1 to 4): ')
    quarter = int(quarter)
    if quarter == 1:
        print('Х > 0 and Y > 0.')
    elif quarter == 2:
        print('Х < 0 and Y > 0.')
    elif quarter == 3:
        print('Х < 0 and Y < 0.')
    elif quarter == 4:
        print('Х > 0 and Y < 0.')
    else:
        print('Error! Try again.')


get_quarter()
