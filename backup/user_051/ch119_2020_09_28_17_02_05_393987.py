import math as mt
def calcula_euler(x,n):
    i=2
    e=1+x
    if n > 2:
        while i<n:
            e+=(x**i)/mt.factorial(i)
            i+=1
    return e