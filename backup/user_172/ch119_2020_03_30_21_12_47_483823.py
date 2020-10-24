import math
b=0
a=1
i=0
def calcula_euler (x,n):
    while i<=n:
        b=b+a
        a = (x**i)/math.factorial(i)        
        print (b)
        return b
