def zera_negativos(lista):
    lenght = len(lista)
    i = 0
    while i < lenght:
        if lista[i] < 0:
            lista[i] = 0
        i = i + 1
    return lista