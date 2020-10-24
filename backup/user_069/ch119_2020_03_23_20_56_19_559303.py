import math
def calcula_euler (x,n):
    c = n
    s = 0
    while c >= 0:
        s += x**c/math.factorial(c)
        c -= 1
    return s