import math

def calcula_euler(x,n):
    euler = 0
    for value in range(0,n):
        euler+= x**value/math.factorial(value)

    return euler