from math import sqrt

def calcula_norma(vetor):
    
    vetor_quadrado = []
    
    for dim in vetor:
        vetor_quadrado.append(dim ** 2)
    
    return sqrt(sum(vetor_quadrado))
    