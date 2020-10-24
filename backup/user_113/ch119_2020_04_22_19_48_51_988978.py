import math
def calcula_euler(x, n):
    e=0
    for i in range(n):
        e +=(x**i)/math.factorial(i)
        i += 1
    return e