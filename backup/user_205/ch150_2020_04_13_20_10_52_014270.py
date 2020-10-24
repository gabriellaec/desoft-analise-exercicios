from math import *
def calcula_pi(n):
    contador = 1
    somatoria = 0
    while contador<=n:
        somatoria += 6/(contador**2)
        contador+=1
    return sqrt(somatoria)
     
        