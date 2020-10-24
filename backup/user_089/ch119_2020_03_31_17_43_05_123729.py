import math
def calcula_euler(x,n):
    i = 0
    while i <= n:
        e = [1 + (x**i)/ math.factorial(i)]**(1/2)
        i = i + 1
    return e
