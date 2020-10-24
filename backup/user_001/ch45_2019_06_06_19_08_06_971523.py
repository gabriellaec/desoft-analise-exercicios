def zera_negativos(lista):
    lista_positiva = []
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            lista_positiva.append(lista[i])
        elif lista[i] == 0:
            lista_positiva.append(lista[i])
        elif lista[i] < 0:
            lista_positiva.append(0)
        i += 1
    return lista_positiva