import math
def calcula_euler(x, n):
    for i in range(n):
        e[i]=(x**i)/math.factorial(i)
        i += 1
    return e