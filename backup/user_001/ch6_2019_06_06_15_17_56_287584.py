import math
def encontra_maximo(lista1, lista2, lista3):
    lista_max = []
    for i in lista1:
        maior1 = 0
        if math.fabs(i) > maior1:
            maior1 = math.fabs(i)
            lista_max.append(maior1)
    for e in lista2:
        maior2 = 0
        if math.fabs(e) > maior2:
            maior2 = math.fabs(e)
            lista_max.append(maior2)
    for k in lista3:
        maior3 = 0
        if math.fabs(k) > maior3:
            maior3 = math.fabs(k)
            lista_max.append(maior3)
    norma = max(lista_max)
    return norma