from math import *
def calcula_euler(x, n):
    i = 0
    y = 0
    while i < n:
        y = y +  x**i/factorial(i)
        i += 1
    return y