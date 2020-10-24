import math 
def calcula_pi(n):
    i = 1
    x = 0
    while i <= n:
        x += 6/i**2
        i+=1
    pi = math.sqrt(x)
    return pi