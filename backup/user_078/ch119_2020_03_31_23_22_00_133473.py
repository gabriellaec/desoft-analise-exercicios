import math
def calcula_euler (x, n):
    i=1
    a=0
    b=1
    c=0
    d=1
    while i<=n:
        d=x**a/b
        c=c+d
        i=i+1
        a=a+1
        b=b*(i-1)
    return c