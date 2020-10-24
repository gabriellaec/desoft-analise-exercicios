import math 
def calcula_euler(x, n):
    b=1
    a=1
    while (b<=n):
        a+=x**b/math.factorial(b)
        b+=1
    return a
    
    