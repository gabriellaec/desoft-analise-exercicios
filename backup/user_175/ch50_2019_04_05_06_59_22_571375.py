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

def numero_no_indice(x):
    lista = []
    for t in range(len(x)):
        if t == x[t]:
            lista.append(t)
    return lista