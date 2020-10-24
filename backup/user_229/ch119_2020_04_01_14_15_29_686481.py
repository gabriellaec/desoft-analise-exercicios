import math
def calcula_euler(x,n):
    i = 0
    s = 0
    while i in range(n+1):
        s += (x**i)/math.factorial(i)
    return s