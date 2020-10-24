import math
def calcula_pi(n):
    lista=[]
    for i in range(1,n+1):
        lista.append(6/i**2)
    return math.sqrt(sum(lista))