import math

def calcula_euler(x, n):
    e = 0
    i = 0
    while i<n+1:
        e += (x**n)/math.factorial(n)
        i += 1
    return e