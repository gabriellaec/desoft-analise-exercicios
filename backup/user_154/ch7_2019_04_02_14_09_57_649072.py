import math

def calcula_norma(lista):
    soma = 0
    
    for x in lista:
        soma = soma + x**2
    
    return math.sqrt(soma)