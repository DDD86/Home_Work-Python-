# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

import math

degree = 0
i = 2
n = int(input("Введите число: "))
while n > 0:
    degree = math.log(n, 2)
    if degree % 1 == 0:
        degree = int(degree)
        print(2**degree)
    n -= 1


