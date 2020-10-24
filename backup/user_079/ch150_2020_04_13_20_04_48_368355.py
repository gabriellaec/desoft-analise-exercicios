import math

def calcula_pi(x):
    lista=[]
    i = 1
    while i <= x:
        pea = (6/(i**2))
        lista.append(pea)
        i+=1
    return math.sqrt(sum(lista))