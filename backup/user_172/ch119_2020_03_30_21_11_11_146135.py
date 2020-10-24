import math
b=0
a=1
def calcula_euler (x,n):
    i=[1]*n
    while i<=n:
        a = (x**i)/math.factorial(i)
        b=b+a
        print (b)
        return b
