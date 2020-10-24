def zera_negativos(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            lista[i] = 0
            lista2.append(lista[i])
            i += 1
            