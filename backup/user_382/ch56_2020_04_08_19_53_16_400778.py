import math as m 
def calcula_norma(lista):
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    return m.sqrt(sum(lista2))