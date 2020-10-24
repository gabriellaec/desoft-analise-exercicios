import math
def calcula_norma(vetor):
    #Escreva uma função que recebe um vetor de dimensão arbitrária representado por uma lista e devolve a sua norma
    lista = []
    for i in len(vetor):
        i += i**2
        return math.sqrt(i)
