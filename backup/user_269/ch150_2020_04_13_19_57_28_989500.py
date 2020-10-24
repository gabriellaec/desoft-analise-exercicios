import math

def calcula_pi(n):
    i=0
    x=1
    dentro_da_raiz=0
    while i<=n:
        dentro_da_raiz+=6/(x)**2
        x+=1
        i+=1
    return math.sqrt(dentro_da_raiz)