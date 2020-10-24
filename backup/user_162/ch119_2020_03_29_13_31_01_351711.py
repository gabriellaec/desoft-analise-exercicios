import math
def calcula_euler(x, n):
    i = 2
    e = 1 + x
    while i != n:
        e+= (x**i)/math.factorial(i)
        i+=1
    return e