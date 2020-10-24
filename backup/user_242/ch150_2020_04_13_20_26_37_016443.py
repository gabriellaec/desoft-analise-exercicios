import math

def calcula_pi(n):
    contador=1
    soma=0
    while contador<=n:
        soma+=6/(contador**2)
        contador+=1
    pi = math.sqrt(soma)
    return pi
    
   