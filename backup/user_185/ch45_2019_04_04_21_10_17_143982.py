def zera_negativos(lista):
    index = 0
    while index < len(lista):
        if lista[index] < 0:
            lista[index] = 0
        index = index + 1
    return(lista)