import math

def encontra_maximo(matriz):
    lista_final = []
    lista_nova = []
    for lista in matriz:
        if min(lista) < 0:
            for numero in lista:
                lista_nova.append(math.fabs(lista[lista.index(numero)]))
                lista_final.append(max(lista_nova))
        else:
            lista_final.append(max(lista))
        
    return max(lista_final)
