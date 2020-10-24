import math
b=0
a=1
def calcula_euler (x,n):
    i=[0]*n
    a = x**i/math.factorial(i)
    b=b+a
    return b