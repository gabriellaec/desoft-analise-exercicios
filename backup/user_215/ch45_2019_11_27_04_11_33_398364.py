def zera_negativos(lista):
    for i in lista:
        if lista[i] < 0 :
            lista[i] = 0
    return lista