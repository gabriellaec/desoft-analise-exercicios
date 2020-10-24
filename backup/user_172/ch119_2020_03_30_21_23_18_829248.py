import math
def calcula_euler (x,n):
    b=0
    a=0
    i=0
    while i<=n:        
        a = (x**i)/math.factorial(i)        
        b=b+a
        i+=1
    return b
