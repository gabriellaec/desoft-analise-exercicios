import math

def calcula_pi(n):
    i=1
    dentro_da_raiz=0
    while i<=n:
        dentro_da_raiz+=6/(i)**2
        i+=1
    return math.sqrt(dentro_da_raiz)