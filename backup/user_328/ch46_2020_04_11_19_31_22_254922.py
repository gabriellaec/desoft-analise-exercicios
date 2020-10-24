def numero_no_indice(lista):
    numeros = lista
    a = len(numeros)
    i=0
    lista2 = []*a
    while a != i:
        if lista[i] == i:
            lista2.append(lista[i])
            i += 1
        else:
            i += 1
    return lista2
    