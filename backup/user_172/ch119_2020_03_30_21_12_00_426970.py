import math
b=0
a=1
i=0
def calcula_euler (x,n):
    while i<=n:
        a = (x**i)/math.factorial(i)
        b=b+a
        print (b)
        return b
