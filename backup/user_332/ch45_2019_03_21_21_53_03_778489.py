def zera_negativos (lista):
    i = 0
    while(i < len(lista)):
        if (lista[i] < 0):
            lista[i] *= (-1)
            i += 1
        else:
            i += 1
    return(lista)   