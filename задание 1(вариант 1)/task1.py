#задание 1 вариант 1
from math import sqrt


print('X | Y')

x_start = -9
x_end = 9
step = 1

while x_start <= x_end:
    if -9 <= x_start <= -6:
        y = -sqrt(9 - (x_start + 6) ** 2)
        print(x_start, y)
    elif -6 < x_start <= -3:
        y = x_start + 3
        print(x_start, y)
    elif -3 < x_start <= 0:
        y = sqrt(9 - x_start ** 2)
        print(x_start, y)
    elif 0 < x_start <= 3:
        y = 3 - x_start
        print(x_start, y)
    else:
        y = 1/2 * (x_start - 3)
        print(x_start, y)
    x_start = x_start + step
