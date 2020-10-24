def numero_no_indice(lista):
    lista_adjacente = []
    for i in range(len(lista)):
        if lista[i] == i:
            lista_adjacente.append(lista[i])
    return lista_adjacente