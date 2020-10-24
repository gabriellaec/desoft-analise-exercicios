
def calcula_euler(x, n):
    c = 0
    d = 1
    e = 0
    euler = 0
    while c < n:
        euler += (x ** c)/d
        c += 1
        d *= e
        e += 1
    return euler
import math
def calcula_euler(x, n):
    euler = 0
    for value in range (0, n):
        euler += x**value/ math.factorial(value)
    return euler
        