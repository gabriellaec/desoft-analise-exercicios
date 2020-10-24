from math import factorial
def calcula_euler(x,n):
    i=0
    e_x = 0
    while i<n:
        f = factorial(i)
        e_x += x**i/f
        i+=1
    return e_x