import math
from random import randint

def subtracao_de_listas (lista1,lista2):
    i=0
    g=0
    t1=len(lista1)
    t2=len(lista2)
    while i<=t2:
        while g<=t1:
            
            if lista1[g]!=lista2[i]:
                g=g+1
            else:
                del lista1[g]
        i=i+1
        g=0
    return lista1 