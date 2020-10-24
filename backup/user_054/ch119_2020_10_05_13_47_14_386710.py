import math
i = x**y/math.factorial(y)

def calcula_euler(x, n):
    e = 1 + x + i
    while n > 0:
        i = i + i
    return  calcula_euler

    