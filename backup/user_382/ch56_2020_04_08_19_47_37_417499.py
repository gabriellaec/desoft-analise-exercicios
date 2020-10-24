import math as m 
def calcula_norma(lista):
    lista2 = []
    for i in lista:
        lista2.append(i**2)
        lista2 = m.sqrt(sum(lista2))
    return lista2