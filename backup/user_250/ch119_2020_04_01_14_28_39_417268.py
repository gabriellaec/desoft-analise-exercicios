import math
def  calcula_euler(x,n):
    i = 1
    s = 0
    while i < n:
        s += 1+x+((x**i)/math.factorial(i))
        i += 1
        return s