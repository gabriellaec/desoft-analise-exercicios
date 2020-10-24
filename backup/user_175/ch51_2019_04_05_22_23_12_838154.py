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

def estritamente_crescente(x):
    lista = [x[0]]
    maior = x[0]
    for i in range(0,len(x)):
        if x[i] > maior:
            lista.append(x[i])
            maior = x[i]
    return lista