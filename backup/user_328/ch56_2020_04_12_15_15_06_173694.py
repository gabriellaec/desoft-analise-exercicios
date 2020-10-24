# norma de um vetor com n termos /v/ = (x**2 + .... + n**2) ** 1/2

import math 

def calcula_norma(vetor):
    final = 0
    for i in vetor:
        final += (i**2)**1/2
    return final