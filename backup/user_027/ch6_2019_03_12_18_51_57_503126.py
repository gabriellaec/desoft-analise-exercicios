from random import *
from math import *
def max_lista(L):
    t = 0
    maximo = L[0]
    while t < len(L):
        if abs(maximo) <= abs(L[t]):
            maximo = L[t]
        t = t + 1
    return maximo

def encontra_maximo(M):
    t = 0
    Max = max_lista(M[0])
    while t < len(M):
        if abs(Max) <= abs(max_lista(M[t])):
            Max = max_lista(M[t])
        t += 1
    return Max