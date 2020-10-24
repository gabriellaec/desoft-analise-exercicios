import math

def calcula_euler(x,n):
    i = 0
    e = 0
    while i < n:
        e += (x**i) / (math.exp(i))
        i +=1 
    return e 