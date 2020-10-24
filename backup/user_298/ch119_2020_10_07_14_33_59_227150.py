import math
def calcula_euler(x,n):
    t = 0
    euler  = 0
    for t in range(0,n):
        euler += (x**t)/(math.factorial(t))
    return euler
#outra forma
"""
def fatorial(n):
    t = 1
    fat = 1 
    while t <= n:
        fat = fat*t
        t += 1
    return fat 


def calcula_euler(x,n):
    t = 1
    e = 1
    while t < n:
        e += (x**t)/fatorial(t) 
        t += 1
    return e"""