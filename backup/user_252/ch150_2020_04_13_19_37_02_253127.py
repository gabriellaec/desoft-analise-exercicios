import math
def calcula_pi(n):
    i=1
    y=1
    while i < n:
        y+=((6/i**2))
        math.sqrt(y)
        i+=1
    return y
    
    