import math
def calcula_euler (x,n):
    c = n
    s = 0
    while c < -1:
        s += x**c/factorial(c)
        c -= 1
    return s