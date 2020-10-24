import math
def calcula_norma(v):
    resultado = 0
    for i in v:
        resultado += i**2
       
    return math.sqrt(resultado)