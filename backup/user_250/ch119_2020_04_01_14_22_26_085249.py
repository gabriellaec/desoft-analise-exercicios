import math
def  calcula_euler(x,n):
    i = 0
    s = 0
    while i < n:
        s += 1+((n**i)/math.factorial(i))
        i += 1
        return s