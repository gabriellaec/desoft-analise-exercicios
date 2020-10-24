import math

def calcula_euler(x,n):
    x = 2
    calcula_euler = 0
    for i in range(n):
        calcula_euler += x**i/math.factorial(i)
    
    return calcula_euler