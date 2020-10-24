import math
def calcula_pi(n):
    a=1
    b=0
    while a<=n:
        b+= 6/a**2
        a+=1
    x=math.sqrt(b)
    return x
        