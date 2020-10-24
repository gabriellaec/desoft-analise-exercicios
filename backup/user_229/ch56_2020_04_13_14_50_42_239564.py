from math import *
def calcula_norma(v):
    norma = 0
    for i in v: 
        norma += i**2
    return (norma**(1/2))