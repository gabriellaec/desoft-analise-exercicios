import math
def  calcula_euler(x,n):
    i = 0
    s = 1
    while i < n:
        s += x+((x**i)/math.factorial(i))
        i += 1
        return s