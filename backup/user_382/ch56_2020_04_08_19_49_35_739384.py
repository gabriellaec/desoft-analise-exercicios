import math as m 
def calcula_norma(lista):
    lista2 = []
    lista3 = []
    for i in lista:
        lista2.append(i**2)
        lista3.append(m.sqrt(sum(lista2)))
    return lista3