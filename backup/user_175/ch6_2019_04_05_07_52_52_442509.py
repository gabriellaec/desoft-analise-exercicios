from random import *
from math import *
def gera_vetor(x): # "x" é a dimensão do vetor.
    x = int(x)
    i = 0
    vetor=[0]*x
    inter = randint(1,(10*x))
    while i < len(vetor):
        vetor[i] = randint(-inter,inter)
        i = i + 1
    return vetor

def max_lista(L):
    t = 0
    maximo = L[0]
    while t < len(L):
        if maximo <= L[t]:
            maximo = L[t]
        t = t + 1
    return maximo

def encontra_maximo(M):
    t = 0
    Max = max_lista(M[0])
    while t < len(M):
        if Max <= max_lista(M[t]):
            Max = max_lista(M[t])
        t += 1
    return Max