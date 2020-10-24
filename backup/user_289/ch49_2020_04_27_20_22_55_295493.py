import math
def inverte_lista(lista):
    lista_invertida = []
    i = -1
    while math.abs(i) <= len(lista):
        lista_invertida.append(lista[i])
        i -= 1
    return lista_invertida