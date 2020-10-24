import math
def calcula_pi(n):
    y=0
    for i in range (1, n+1):
        y+=6/(i**2)
    x=math.sqrt(y)
    return x