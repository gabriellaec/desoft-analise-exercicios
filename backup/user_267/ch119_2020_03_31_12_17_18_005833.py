from math import factorial
def calcula_euler(x,n):
    i=0
    f = factorial(i)
    while i<n:
        e_x= x**i/f
        i+=1
    return e_x