from math import factorial
def fatorial(x):
    math.factorial(x)
    
def calcula_euler(x,n):
    euler=1
    for y in range (1,n):
        euler+=x**y/fatorial(y)
    return euler