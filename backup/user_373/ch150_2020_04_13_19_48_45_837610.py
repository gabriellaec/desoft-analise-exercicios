import math
def calcula_pi(n):
    i=1
    y= 0
    while i<= n:
        y+= 6/i**2
        i+=1
    z= math.sqrt(y)
    return z