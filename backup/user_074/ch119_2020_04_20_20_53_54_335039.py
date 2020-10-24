import math
def calcula_euler(x,n):
    i=0
    while i<=n:
        e+=x**i/math.fatorial(i)
        i+=1      
    return e