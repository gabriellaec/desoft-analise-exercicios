def encontra_maximo(matriz):
    lista_max = []
    for lista in matriz:
        lista_max.append(max(lista))
        
    return max(lista_max)