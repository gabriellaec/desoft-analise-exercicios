from math import *
def calcula_fibonacci(numero):
    lista = [0]*abs(numero)
    lista[0]=1
    lista[1]=1
    i = 2
    while i < abs(numero):
        lista[i]=lista[i-1]+lista[i-2]
        i+=1
    return lista