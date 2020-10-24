def zera_negativos(lista):
    for i in range(len(lista)+1):
        if lista[i] < 0:
            lista[i] = 0 
    return lista
