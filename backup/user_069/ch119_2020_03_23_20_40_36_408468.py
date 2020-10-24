import math
def calcula_euler (x,n):
    c = n
    s = 1
    while c < 0:
        s += x**c/factorial(c)
        c -= 1