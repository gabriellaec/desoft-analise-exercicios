import math

def calcula_euler(x, n):
    e = 1 
    i = 1
    while n > i:
        y = x**i/math.factorial(i)
        i+=1
        e = e + y
    return  e

    