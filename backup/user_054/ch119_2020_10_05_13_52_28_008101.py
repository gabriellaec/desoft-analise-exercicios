import math
y = x**x/math.factorial(x)
i = 2
def calcula_euler(x, n):
    e = 1 + x + i
    while n < i:
        y[i] = y[i-1] + e
    return  calcula_euler

    