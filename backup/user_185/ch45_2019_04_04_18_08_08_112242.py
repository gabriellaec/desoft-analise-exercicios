def zera_negativos(lista):
    index = 0
    while index < len(lista):
        if lista[index] < 0:
            lista[index] = 0
    return(lista)