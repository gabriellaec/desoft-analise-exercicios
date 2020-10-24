from math import factorial
def fatorial(x):
    factorial(x)
    
def calcula_euler(z,n):
    euler=1
    for y in range (1,n):
        euler+=z**y/fatorial(y)
    return euler