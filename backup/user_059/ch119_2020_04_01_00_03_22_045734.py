import math as m

def calcula_euler(x, n):
    i = 0
    while i<n:
        euler = ((x**i)/m.factorial(i))
        i+=1
    return (euler+1+x)