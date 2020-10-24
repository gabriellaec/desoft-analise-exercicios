import math
def calcula_pi (n):
    i=1
    p=0
    while i<=n:
        p+=6/(i**2)
        i+=1
    pin=math.sqrt(p)
    return pin