import math

def calcula_norma (lista):
    i=0
    soma2=0

    while(i<len(lista)):
        soma2+=(lista[i])**2
        i+=1

    return math.sqrt(soma2)