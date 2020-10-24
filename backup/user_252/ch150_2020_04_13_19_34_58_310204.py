import math
def calcula_pi(n):
    i=1
    y=0
    while i <= n:
        y+=math.sqrt((6/i**2))
        i+=1
    return y
    
    