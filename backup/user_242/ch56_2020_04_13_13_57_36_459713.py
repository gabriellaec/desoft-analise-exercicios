import math
def calcula_norma(lista):
    lista2=[]
    for i in lista:
        lista2.append(i**2)
    return math.sqrt(sum(lista2))