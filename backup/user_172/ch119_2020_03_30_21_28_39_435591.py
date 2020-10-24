import math
def calcula_euler (x,n):
    b=0
    a=1
    i=1
    while i<=n:        
        a = (x**i)/math.factorial(i)        
        b=b+a
        i+=1
    return b
