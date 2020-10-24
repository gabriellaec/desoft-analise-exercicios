i = 0
import math
def calcula_euler(x,n):
    while i <= n:
        e = [1 + (x**i)/ math.factorial(i)]**(1/2)
        i = i + 1
    return e
