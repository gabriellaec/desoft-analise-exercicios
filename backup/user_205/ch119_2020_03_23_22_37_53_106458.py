from math import factorial
def calcula_euler(x,n):
    for i in range(1,n):
        z = 1 + x + (x**i)/factorial(i)
        return z
   