import math
def  calcula_euler(x,n):
    i = 1
    s = 1
    while i < n:
        s += ((x**i)/math.factorial(i))
        i += 1
        return s