import math

def calcula_euler(x, n):
    e = 0
    i = 0
    while i<n:
        e += (x**i)/math.factorial(i)
        i += 1
    return e