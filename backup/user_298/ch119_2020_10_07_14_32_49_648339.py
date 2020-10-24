import math
def calcula_euler(x,n):
    t = 0
    euler  = 0
    while t < n:
        euler += (x**t)/(math.factorial(t))
        t += 1
    return euler

