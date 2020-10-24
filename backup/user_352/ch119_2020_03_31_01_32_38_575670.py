import math 
def calcula_euler(x, n):
    b=0
    a=0
    while (b<n):
        a+=x**b/math.factorial(b)
        b+=1
    return a
    
    