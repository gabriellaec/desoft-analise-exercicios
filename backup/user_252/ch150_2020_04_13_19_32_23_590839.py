import math
def calcula_pi(n):
    i=1
    y=0
    for i in n:
        y+=math.sqrt((6/i)**2)
        i+=1
    return y
    
    