def zera_negativos(lista):
    for i in lista:
        if i < 0 :
            lista[i] = 0
    return lista