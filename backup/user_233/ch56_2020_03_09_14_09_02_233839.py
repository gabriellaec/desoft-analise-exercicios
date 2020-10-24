from math import sqrt

def square(n): return n ** 2

def calcula_norma(vetor):
    
    return sqrt(sum(vetor.map(square)))