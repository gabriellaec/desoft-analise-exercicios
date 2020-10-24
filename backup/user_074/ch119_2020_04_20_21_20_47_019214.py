import math
def calcula_euler(x,n):
    i=1
    e=1
    while i<=n:
        e+=x**i/math.factorial(i)
        i+=1      
    return e